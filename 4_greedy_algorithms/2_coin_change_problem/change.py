def change(input) -> int:
    coins: list[int] = input['coins']
    V: int = input['value']
    coins.sort(reverse=True)
    number = 0

    for coin in coins:
        while coin <= V:
            number += 1
            V -= coin
            
            if V == 0:
                break

    return number

if __name__ == "__main__":
    ## Expected result 5
    print(change({"value": 47, "coins": [1, 5, 10, 25]}))