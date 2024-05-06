def change(input) -> int:
    coins:list = input['coins']
    V:int = input['value']
    # Filter out negative values from coins array
    coins = [coin for coin in coins if coin > 0]
    # Initialize dynamic programming table
    dp = [0] + [float('inf')] * V
    # Update dp array for each value using map() and min()
    for value in range(1, V + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)
    return dp[V]