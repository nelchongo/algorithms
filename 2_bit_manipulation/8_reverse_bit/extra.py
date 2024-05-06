def reverse_bits(num):
    reversed_num = 0
    num_bits = 32  # Assuming 32-bit integers

    for i in range(num_bits):
        # Shift the reversed number to the left by 1
        reversed_num <<= 1
        
        # Extract the least significant bit from 'num' and append it to 'reversed_num'
        if num & 1:
            reversed_num |= 1

        # Right shift 'num' by 1 to process the next bit
        num >>= 1

    return reversed_num

# Reverse bits for numbers from 1 to 10
for i in range(1, 11):
    print(f"Reverse of {i}: {reverse_bits(i)}")
