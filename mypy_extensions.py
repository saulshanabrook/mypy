# Simple mypy_extensions stub
def mypyc_attr(*args, **kwargs):
    def decorator(cls):
        return cls
    return decorator

def trait(cls):
    return cls

class FlexibleAlias:
    pass