def fibonacci(input: int) -> list[int]:
    sequence = []
    for n in range(0, input + 1):
        if n < 2:
            sequence.append(n)
            continue
        sequence.append(sequence[n - 1] + sequence[n - 2])

    return sequence