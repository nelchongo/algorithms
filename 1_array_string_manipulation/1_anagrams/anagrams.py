def anagrams(string_list: list[str]) -> bool:
    string_1 = string_list[0].replace(" ", "")
    string_2 = string_list[1].replace(" ", "")

    if (len(string_1) == len(string_2)):
        compare:dict = {}
        for n in range(0, len(string_1)):
            compare[string_1[n]] = compare.get(string_1[n], 0) + 1
            compare[string_2[n]] = compare.get(string_2[n], 0) + 1
        return not(1 in compare.values())
    return False