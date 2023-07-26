def mergesort(arr, l, r):
    if len(arr) <= 1:
        return arr
    m = (r - l) // 2
    left, lc = mergesort(arr, l, m)
    right, rc = mergesort(arr, m+1, r)
    merged, c = merge(left ,right)
    return merged, lc + rc + c

def merge(left, right):
    i = 0
    j = 0
    
    newArr = []
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            newArr.append(left[i])
            i += 1
        else:
            newArr.append(right[j])
            count += len(left) - i 
            j += 1

    newArr.extend(left[i:]) 
    newArr.extend(right[j:]) 
    return newArr, count

    




