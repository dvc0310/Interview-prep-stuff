def merge_with_smaller_auxiliary_array(a, aux, N):
    for k in range(N):
        aux[k] = a[k]
    
    i = 0
    j = N
    k = 0
    while k < len(a):
        if i >= N:
            a[k] = a[j]
            j += 1
        elif j >= len(a):
            a[k] = aux[i]
            i += 1
        elif aux[i] < a[j]:
            a[k] = aux[i]
            i += 1
        else:
            a[k] = a[j]
            j += 1
        k += 1

if __name__ == "__main__":
    a = [40, 61, 70, 71, 99, 20, 51, 55, 75, 100]
    N = len(a) // 2
    aux = [0]*N
    merge_with_smaller_auxiliary_array(a, aux, N)
    print("After merging:")
    print(a)

