# Standard Library
import traceback
import io


def email_function_failure_traceback(send_email_function):
    def decorator(original_func):
        def new_func(*args, **kwargs):
            try:
                function_value = original_func(*args, **kwargs)
            except Exception as e:
                exc_string = io.StringIO()
                traceback.print_exc(file=exc_string)
                message = exc_string.getvalue()
                message = message.replace('line ', '<br /><br />line ')
                send_email_function(message)
                raise e
            return function_value
        return new_func
    return decorator
