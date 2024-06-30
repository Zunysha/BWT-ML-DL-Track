# math_pkg/addition.py

def add(a, b):
    """
    Returns the sum of a and b.
    """
    try:
        return a + b
    except TypeError as e:
        raise ValueError("Both arguments must be numbers") from e
# math_pkg/subtraction.py

def subtract(a, b):
    """
    Returns the difference of a and b.
    """
    try:
        return a - b
    except TypeError as e:
        raise ValueError("Both arguments must be numbers") from e
# math_pkg/multiplication.py

def multiply(a, b):
    """
    Returns the product of a and b.
    """
    try:
        return a * b
    except TypeError as e:
        raise ValueError("Both arguments must be numbers") from e
# math_pkg/division.py

def divide(a, b):
    """
    Returns the division of a by b.
    Raises ValueError if b is zero.
    """
    try:
        if b == 0:
            raise ValueError("The divisor must not be zero")
        return a / b
    except TypeError as e:
        raise ValueError("Both arguments must be numbers") from e
# math_pkg/modulus.py

def modulus(a, b):
    """
    Returns the modulus of a by b.
    Raises ValueError if b is zero.
    """
    try:
        if b == 0:
            raise ValueError("The divisor must not be zero")
        return a % b
    except TypeError as e:
        raise ValueError("Both arguments must be numbers") from e
# math_pkg/exponentiation.py

def exponentiate(base, exp):
    """
    Returns the base raised to the power of exp.
    """
    try:
        return base ** exp
    except TypeError as e:
        raise ValueError("Both arguments must be numbers") from e
# math_pkg/square_root.py

import math

def square_root(a):
    """
    Returns the square root of a.
    Raises ValueError if a is negative.
    """
    try:
        if a < 0:
            raise ValueError("The number must be non-negative")
        return math.sqrt(a)
    except TypeError as e:
        raise ValueError("The argument must be a number") from e
