# Simple mypy_extensions stub
def mypyc_attr(*args, **kwargs):
    def decorator(cls):
        return cls
    return decorator

def trait(cls):
    return cls

class FlexibleAlias:
    def __getitem__(self, item):
        return item[0] if isinstance(item, tuple) else item