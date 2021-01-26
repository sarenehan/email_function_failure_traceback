# email_function_failure_traceback
This is a decorator for monitoring errors for remote jobs. Wrap your main function in the `email_function_failure_traceback` decorator, and if the function fails, an email will be sent based on your configuration that includes the traceback of the error (including SQL errors).


# Installation
```bash
pip install email_function_failure_traceback
```

# Functions:
email_function_failure_traceback(send_email_function)


# Examples:
**cache_to_disk**
```python
"""
This example caches the function "my_function" for 3 days.
"""
from functools import partial
from email_function_failure_traceback import email_function_failure_traceback


# Implement this yourself using your preferred Email integration...
def send_email(message, subject_line, to_address, from_address):
    Email(to_address, from_address, subject_line, message)


@email_function_failure_traceback(
    partial(
        send_email,
        subject_line='my function failed',
        to_address='example@example.com',
        from_address='example@example.com'))
def my_function():
    assert 1 == 2


# This will send an email to `example@example.com` with the error traceback.
my_function()
```
