class Solution(object):
    def findDifference(self, nums1, nums2):
        my_dict = dict()
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        i = 0
        while i < len(nums2):
            if nums2[i] not in my_dict:
                my_dict[nums2[i]] = 1
            else:
                my_dict[nums2[i]] += 1
            i += 1

        i = 0
        while i < len(nums1):
            if nums1[i] not in my_dict:
                my_dict[nums1[i]] = 1
            else:
                my_dict[nums1[i]] += 1
            i += 1

        for key, value in my_dict.items():
            if value > 1:
                nums1.remove(key)
                nums2.remove(key)
        return [nums1, nums2]

        
nums1 = [52,-21]
nums2 = [22,66,89,52,-56,5,22,-70,99]
print(Solution().findDifference(nums1, nums2))