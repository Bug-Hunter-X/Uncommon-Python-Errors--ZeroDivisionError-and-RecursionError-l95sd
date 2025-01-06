def function_with_uncommon_error(a, b):
    if a == 0:
        return b / a  # ZeroDivisionError, but only if a is exactly 0
    elif a < 0:
        return function_with_uncommon_error(a + 1, b) # RecursionError if a is a very large negative number
    else:
        return a + b