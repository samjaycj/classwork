class Functions:
    def power (base, exponent=2):
        result = base ** exponent
        return result

    result1 = power(5)
    print(f"Result of 5 raised to the power of 2 is: {result1}")

    result2 = power(2, 4)
    print(f"Result of 2 raised to the power of 4 is: {result2}")

    result3 = power(10, 3)
    print(f"Result of 10 raised to the power of 3 is: {result3}")