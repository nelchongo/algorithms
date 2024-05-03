def anagrams(string_1: str, string_2: str) -> bool:
    if (len(string_1) == len(string_2)):
        compare:dict = {}
        for n in range(0, len(string_1)):
            compare[string_1[n]] = compare.get(string_1[n], 0) + 1
            compare[string_2[n]] = compare.get(string_2[n], 0) + 1
        return not(1 in compare.values())
    return False