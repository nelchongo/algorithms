def selection(activities:list[list[int]]) -> list[list[int]]:
    #Init the selected_activities
    selected_activities:list[list[int]] = []
    #Sort the activities
    activities.sort(key = lambda x: x[1])

    for index, value in enumerate(activities):
        if index == 0:
            selected_activities.append(value)
            continue
        
        if value[0] >= selected_activities[- 1][1]:
            selected_activities.append(value)

    return selected_activities

if __name__ == "__main__":
    test = [[1, 2], [2, 4], [3, 5], [4, 6], [5, 7], [6, 8], [7, 9], [8, 10], [9, 11], [10, 12]]
    print(selection(test))