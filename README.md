# AccuKnox Django Assignment

This is my submission for the Django Trainee position at AccuKnox. The assignment covers Django signals and a custom Python class.

## What's Inside

The project has two parts:
1. Three questions about Django signals behavior
2. One custom Rectangle class in Python

## Project Structure

accuknox-django-assignment/
├── accuknox_project/ # Main Django project
├── signals_demo/ # App with signal tests
│ ├── signals.py
│ └── test_signals.py
├── custom_classes/
│ └── rectangle.py
└── manage.py

## Setup

Clone the repo

git clone <your-repo-url>
cd accuknox-django-assignment
Create virtual environment

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Install Django

pip install -r requirements.txt
Run migrations

python manage.py migrate


## Running the Tests

**For Django Signals:**

python manage.py test signals_demo.test_signals -v 2


**For Rectangle Class:**

python custom_classes/rectangle.py


## Answers

### Question 1: Are Django signals synchronous or asynchronous?

**Answer: Synchronous**

Django signals run synchronously by default. The caller waits for the signal to finish before moving forward.

I tested this by adding a 3-second sleep in the signal handler. The total execution time was around 3 seconds, proving that the code waited for the signal to complete.

### Question 2: Do signals run in the same thread?

**Answer: Yes**

Signals run in the same thread as the caller.

I verified this by printing `threading.current_thread().ident` from both the caller and the signal handler. Both showed the same thread ID.

### Question 3: Do signals run in the same database transaction?

**Answer: Yes**

When you wrap code in `transaction.atomic()`, signals run in that same transaction.

I proved this by raising an exception in the signal handler. This caused the entire transaction to rollback, including the database save that triggered the signal. After the rollback, the user I tried to create didn't exist in the database.

### Question 4: Rectangle Class

Created a Rectangle class that takes length and width as parameters. Made it iterable using `__iter__` method with yield statements.

class Rectangle:
def init(self, length: int, width: int):
self.length = length
self.width = width

def __iter__(self):
    yield {'length': self.length}
    yield {'width': self.width}


When you iterate over it:

rect = Rectangle(10, 5)
for item in rect:
print(item)
Output:
{'length': 10}
{'width': 5}


## Technologies Used

- Python 3.8+
- Django 4.2+
- SQLite

## Notes

All the code is tested and working. The test cases print detailed output so you can see exactly what's happening with the signals.

---

Made for AccuKnox Django Trainee Assignment