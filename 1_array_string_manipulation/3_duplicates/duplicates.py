def duplicates(arr: list) -> list[int]:
    return list(set([x for x in arr if arr.count(x) > 1]))