import inspect
from functools import wraps


def not_none_arg(arg_name):
    def decorator(func):
        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()

            # TODO: Добавить проверку есть ли у функции аргмент arg_name
            if bound.arguments[arg_name] is None:
                return None

            return func(*args, **kwargs)

        return wrapper

    return decorator
