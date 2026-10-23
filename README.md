# Number Pattern Generator

## Description

A Python function that generates a number pattern from 1 to a user-defined value. The program validates input to ensure the argument is a positive integer and returns helpful error messages when invalid data is provided.

This project demonstrates fundamental Python programming concepts, including:

- Functions
- Input validation
- Conditional statements
- Loops
- String manipulation
- Type checking

## Code

```python
def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'

    pattern = ''

    for number in range(1, n + 1):
        pattern = pattern + str(number) + ' '

    return pattern.strip()
```

## Usage

```python
print(number_pattern(5))
```

### Output

```text
1 2 3 4 5
```

## Examples

### Valid Input

```python
number_pattern(3)
```

Output:

```text
1 2 3
```

### Invalid Type

```python
number_pattern("3")
```

Output:

```text
Argument must be an integer value.
```

### Invalid Value

```python
number_pattern(0)
```

Output:

```text
Argument must be an integer greater than 0.
```

## Learning Objectives

This project was created to practise:

- Writing Python functions
- Working with loops
- Validating user input
- Building and returning strings
- Using built-in functions such as `isinstance()`

