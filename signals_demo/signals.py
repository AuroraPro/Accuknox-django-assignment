import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Question 1: Synchronous execution proof
@receiver(post_save, sender=User)
def synchronous_signal_handler(sender, instance, created, **kwargs):
    """This handler proves signals are synchronous"""
    if created and instance.username.startswith('sync_'):
        print(f"[SIGNAL] Started at {time.time()}")
        time.sleep(3)  # Simulate slow operation
        print(f"[SIGNAL] Finished at {time.time()}")


# Question 2: Same thread proof
@receiver(post_save, sender=User)
def thread_signal_handler(sender, instance, created, **kwargs):
    """This handler proves signals run in same thread"""
    if created and instance.username.startswith('thread_'):
        print(f"[SIGNAL] Thread ID: {threading.current_thread().ident}")
        print(f"[SIGNAL] Thread Name: {threading.current_thread().name}")


# Question 3: Transaction proof
@receiver(post_save, sender=User)
def transaction_signal_handler(sender, instance, created, **kwargs):
    """This handler proves signals run in same transaction"""
    if created and instance.username == 'transaction_test':
        print("[SIGNAL] Signal handler executing")
        raise Exception("Intentional error to test transaction rollback")
