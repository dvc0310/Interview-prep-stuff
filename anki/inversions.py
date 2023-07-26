def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0
    m = len(arr) // 2
    left, inv_left = mergesort(arr[:m])
    right, inv_right = mergesort(arr[m:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge

def merge(left, right):
    i = 0
    j = 0
    newArr = []
    inv_count = 0  
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            newArr.append(left[i])
            i += 1
        else:
            newArr.append(right[j])
            inv_count += len(left) - i 
            j += 1
    newArr.extend(left[i:])
    newArr.extend(right[j:])
    return newArr, inv_count 

        

