def fibonacci(input:int, sequence:list[int] = None, index:int = 0) -> list[int]:
    sequence = [] if sequence is None else sequence

    if index <= input:
        if index < 2:
            sequence.append(index)
        else:
            sequence.append(sequence[index - 1] + sequence[index - 2])
        return fibonacci(input, sequence, index + 1)
    return sequence