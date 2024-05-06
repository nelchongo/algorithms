def fibonacci(input: int) -> int:
    if input < 2:
        return input
    return recursive(input)

def recursive(input:int, value:int = 1, prev_value:int = 0, index:int = 2) -> int:
    if index < input:
        return recursive(input, value + prev_value, value, index + 1)
    return value + prev_value