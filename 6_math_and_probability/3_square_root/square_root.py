def square_root(input:int, threshold:float = 0) -> int:
    if input == 0 : return 0
    threshold = threshold if threshold > 0 else 0.00000001
    # Using the Newton-Raphson method
    # We initialized in input/2 is the first
    x = input / 2
    x = raphson(x, input, threshold)
    return round(x, 5)

def raphson(x:float, s:int, threshold:float) -> float:
    x_new = (1/2)*(x + (s/x))
    if abs(x - x_new) < threshold:
        return x
    return raphson(x_new, s, threshold)