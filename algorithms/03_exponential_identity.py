def calculate_square_root(exponential_identity):
    """
    Calculate the square root using the exponential identity.

    Parameters:
    - exponential_identity (float): Number for which the square root will be calculated.

    Returns:
    - float: Result of the square root.
    """
    square_root_result = exponential_identity ** 0.5
    return square_root_result

if __name__ == "__main__":
    # Example of usage
    number = 25
    result = calculate_square_root(number)
    print(f"The square root of {number} is: {result}")