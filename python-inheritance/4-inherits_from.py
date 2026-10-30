#!/usr/bin/python3
""""check if function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class; otherwise False."""

def inherits_from(obj, a_class):
    """If an obj is an instance of a class that inherited
    (directly or indirectly) from the specific a_class."""

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
