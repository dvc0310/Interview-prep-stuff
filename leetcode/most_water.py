class Solution(object):
    def maxArea(self, height):
        max_so_far = 0
        i, j = 0, len(height) - 1

        while i < j:
            current_min_height = min(height[i], height[j])
            width = j - i
            current_area = current_min_height * width
            max_so_far = max(max_so_far, current_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_so_far

            
