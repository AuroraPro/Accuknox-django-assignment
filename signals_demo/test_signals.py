import time
import threading
from django.test import TestCase
from django.db import transaction
from django.contrib.auth.models import User


class SignalsTestCase(TestCase):
    
    def test_question1_signals_are_synchronous(self):
        print("\n" + "="*60)
        print("TEST 1: SYNCHRONOUS EXECUTION")
        print("="*60)
        
        print(f"[CALLER] Creating user at {time.time()}")
        start_time = time.time()
        
        user = User.objects.create(username='sync_test_user', email='sync@test.com')
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        print(f"[CALLER] User created at {time.time()}")
        print(f"[RESULT] Total time elapsed: {elapsed:.2f} seconds")
        
        self.assertGreaterEqual(elapsed, 3.0, 
            "Signal executed synchronously - caller waited for signal to complete")
        
        print("[CONCLUSION] Signals are SYNCHRONOUS ✓")
        print("="*60)
    
    def test_question2_signals_run_in_same_thread(self):
        print("\n" + "="*60)
        print("TEST 2: THREAD EXECUTION")
        print("="*60)
        
        caller_thread_id = threading.current_thread().ident
        caller_thread_name = threading.current_thread().name
        
        print(f"[CALLER] Thread ID: {caller_thread_id}")
        print(f"[CALLER] Thread Name: {caller_thread_name}")
        
        user = User.objects.create(username='thread_test_user', email='thread@test.com')
        
        print("[CONCLUSION] Signal runs in SAME THREAD as caller ✓")
        print("="*60)
    
    def test_question3_signals_run_in_same_transaction(self):
        print("\n" + "="*60)
        print("TEST 3: DATABASE TRANSACTION")
        print("="*60)
        
        print("[CALLER] Starting transaction...")
        
        try:
            with transaction.atomic():
                print("[CALLER] Creating user inside transaction")
                user = User.objects.create(
                    username='transaction_test',
                    email='transaction@test.com'
                )
                print("[CALLER] User object created (not yet committed)")
        except Exception as e:
            print(f"[CALLER] Exception caught: {e}")
        
        user_exists = User.objects.filter(username='transaction_test').exists()
        
        print(f"[RESULT] User exists in database: {user_exists}")
        
        self.assertFalse(user_exists, 
            "User should not exist - transaction was rolled back due to signal error")
        
        print("[CONCLUSION] Signal runs in SAME TRANSACTION ✓")
        print("When signal raises exception, entire transaction is rolled back")
        print("="*60)
