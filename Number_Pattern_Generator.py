# Number Pattern Generator
def number_pattern(n):
    # Check that the argument is an integer.
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    # Check that the integer is greater than 0.
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    # Create an empty string to store the pattern.
    pattern = ''

    # Loop through the numbers from 1 up to and including n.
    for number in range(1, n + 1):
        # Add the current number and a space to the pattern.
        pattern = pattern + str(number) + ' '

    # Remove the extra space at the end and return the result.
    return pattern.strip()