#!/usr/bin/python3
"""Function to check if object inherits from specified class"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class a_class.
    """
    # Traverse the inheritance chain of obj's class
    current_class = obj.__class__
    while current_class is not None:
        # Check if the current class is the specified class or its subclass
        if current_class is a_class:
            return True
        # Move up the inheritance chain
        current_class = current_class.__base__
    return False
