# main.py

import math_pkg


def main():
    try:
        # Basic arithmetic operations
        print("Addition: "+ str(math_pkg.add(5, 3)))
        print("Subtraction: "+ str(math_pkg.subtract(5, 3)))
        print("Multiplication: "+ str(math_pkg.multiply(5, 3)))
        print("Division: "+ str(math_pkg.divide(6, 3)))
        print("Modulus: "+ str(math_pkg.modulus(5, 3)))

        # Advanced mathematical operations
        print("Exponent: "+ str(math_pkg.exponentiate(2, 3)))
        print("Square Root: " + str(math_pkg.square_root(16)))

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
