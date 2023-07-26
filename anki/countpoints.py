def countPoints(arr1, arr2):
    hashmap = {}
    for point in arr1:
        if point not in hashmap:
            hashmap[point] = 1

    for point in arr2:
        if point not in hashmap:
            hashmap[point] = 1
        else:
            hashmap[point] += 1

    count = 0
    lst = []
    for key, value in hashmap.items():
        if value > 1:
            count += 1
            lst.append(key)
    return count



