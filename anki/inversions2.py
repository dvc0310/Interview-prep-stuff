class Solution:
    def mergesort(self, arr, l, r):
        if len(arr) <= 1:
            return arr
        
        m = (l+r) // 2
        left, lc = self.mergesort(arr, l, m)
        right, rc = self.mergesort(arr, m+1, r)

        merged, mc = self.merge(left, right)
        return merged, lc + rc + mc

    def merge(self, left, right):
        l = 0
        r = 0
        arr = []
        count = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr.append(left[l])
                l += 1
            else:
                arr.append(right[r])
                count += len(left) - l
                r += 1

        arr.extend(left[l:])
        arr.extend(right[r:])

        return arr, count
