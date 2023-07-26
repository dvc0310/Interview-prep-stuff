
def threesum(A):
    A.sort()
    i = 0
    lst = []
    while i < len(A) - 1:
        l = i + 1
        r = len(A) - 1
        
        while l < r:
            sum = A[i] + A[l] + A[r]
            if sum == 0:
                lst.append((A[i], A[l], A[r]))
                l+=1
                r-=1
            elif sum < 0:
                l+=1
            else:
                r-=1
            while A[l] == A[l+1]:
                    l+=1
            while A[r] == A[r-1]:
                    r-=1
        
        i += 1
    return lst
        
A = [10, 5, -8, 7, 2, -2,-5]
print(threesum(A))