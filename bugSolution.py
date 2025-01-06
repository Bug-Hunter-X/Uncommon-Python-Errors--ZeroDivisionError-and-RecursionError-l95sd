def function_with_error_handling(a, b):
    try:
        if abs(a) < 1e-9:  # Check for near-zero values to avoid floating-point issues
            raise ZeroDivisionError("a is too close to zero")
        elif a < 0:
            # Limit recursion depth
            if a < -1000:
                raise RecursionError("Recursion depth exceeded")
            return function_with_error_handling(a + 1, b)
        else:
            return a + b
    except (ZeroDivisionError, RecursionError) as e:
        print(f"Error: {e}")
        return None  # Or handle the error in a more appropriate way