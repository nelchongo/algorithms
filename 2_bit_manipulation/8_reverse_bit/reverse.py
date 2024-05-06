#ASUMING IN A 32 BITS SCENARIO
def reverse(input: int) -> int:
    b_string = bin(input)[2:]
    bits = len(b_string)
    #Adding missing bits to the binary sequence
    if bits < 32:
        missing_bits = '0' * (32 - bits)
        b_string = missing_bits + b_string

    return int(b_string[::-1], 2)