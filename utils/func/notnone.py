import inspect
from functools import wraps


def not_none(func):
    signature = inspect.signature(func)
    parameters = signature.parameters
    # TODO: Добавить обработку ситуации если пользователь использует
    # нестандартные именно вместо cls или self

    if not parameters or (
        ("self" in parameters or "cls" in parameters) and len(parameters) == 1
    ):
        raise ValueError(f"Функция {func.__name__} не имеет аргументов")

    param_iter = iter(parameters)

    if "self" in parameters or "cls" in parameters:
        next(param_iter)
    first_arg_name = next(param_iter)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()

        value = bound.arguments[first_arg_name]

        if value is not None:
            return func(*args, **kwargs)

        return None

    return wrapper
