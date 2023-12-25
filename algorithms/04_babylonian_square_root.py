def babylonian_square_root(a, initial_approximation=1.0, tolerance=1e-10, max_iterations=100):
    """
    Calculate the square root of a number using the Babylonian method.

    Parameters:
    - a (float): The number for which the square root is to be calculated.
    - initial_approximation (float): Initial guess for the square root (default is 1.0).
    - tolerance (float): Tolerance level to determine convergence (default is 1e-10).
    - max_iterations (int): Maximum number of iterations (default is 100).

    Returns:
    - float: Approximation of the square root.

    Raises:
    - RuntimeError: If no convergence is achieved within the maximum number of iterations.
    """
    x_n = initial_approximation

    for _ in range(max_iterations):
        x_n_plus_1 = 0.5 * (x_n + a / x_n)

        if abs(x_n_plus_1 - x_n) < tolerance:
            return x_n_plus_1

        x_n = x_n_plus_1

    raise RuntimeError("No convergence within the maximum number of iterations.")

# Example of usage
number = 25
result = babylonian_square_root(number)
print(f"The square root of {number} is approximately: {result}")