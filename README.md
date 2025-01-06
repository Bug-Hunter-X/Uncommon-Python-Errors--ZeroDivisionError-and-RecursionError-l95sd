# Uncommon Python Errors

This repository demonstrates two uncommon Python errors that can be tricky to debug:

1. **ZeroDivisionError:** This occurs when attempting to divide by zero.  The example code handles the case where 'a' is 0, but a more robust solution would check for 'a' being close to zero to avoid floating-point inaccuracies.
2. **RecursionError:** This happens when a recursive function calls itself too many times, exceeding the maximum recursion depth.  The example code shows how a large negative input for 'a' can trigger this.

The solution file provides a more robust and error-handled version.