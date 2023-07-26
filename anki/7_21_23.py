# Helper function to find two numbers that add up to a given target.
def twoSum(subarray, target):
    num_to_index = {}
    for index, num in enumerate(subarray):
        complement = target - num  # The number needed to reach the target.
        if complement in num_to_index:
            # If the complement exists, a pair that adds to the target has been found.
            # Return the indices of the pair.
            return [num_to_index[complement], index]
        else:
            # If not, store this number and its index.
            num_to_index[num] = index
    # If no pair found, return an empty list.
    return []

# Main function to find four numbers that add up to a given target.
def fourSum(nums, target):
    # Sort the array to handle duplicates.
    nums.sort()
    
    # Initialize the list to store the result.
    quadruplets = []

    # Loop through the array.
    for first_index in range(len(nums) - 3):
        # Skip duplicate numbers.
        if first_index > 0 and nums[first_index] == nums[first_index - 1]:
            continue

        for second_index in range(first_index + 1, len(nums) - 2):
            # Skip duplicate numbers.
            if second_index > first_index + 1 and nums[second_index] == nums[second_index - 1]:
                continue

            # The target for twoSum would be remaining sum after considering the first two numbers.
            two_sum_target = target - nums[first_index] - nums[second_index]
            
            # Apply twoSum on the rest of the array.
            subarray = nums[second_index + 1:]
            two_sum_indices = twoSum(subarray, two_sum_target)
            
            # If a pair is found, add all four numbers to the result.
            if two_sum_indices:
                third_index_relative, fourth_index_relative = two_sum_indices
                # Convert relative indices to indices in the original array.
                third_index = third_index_relative + second_index + 1
                fourth_index = fourth_index_relative + second_index + 1
                quadruplet = [nums[first_index], nums[second_index], nums[third_index], nums[fourth_index]]
                if quadruplet not in quadruplets:
                    quadruplets.append(quadruplet)

    return quadruplets



nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums, target))


arr = ['a', 'c', 'f', 'h']
key = 'h'

def nextLetter(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if ord(arr[m]) == ord(key):
            next_idx = (m + 1) % len(arr)
            return arr[next_idx]
        if ord(arr[m]) < ord(key):
            l = m + 1
        else:
            r = m - 1
        
    return arr[l % len(arr)]


print(nextLetter(arr, key))

def canJump(nums):
    n = len(nums)
    last_position = n - 1
    for i in range(n-1, -1, -1):
        if i + nums[i] >= last_position:
            last_position = i
    return last_position == 0


nums = [2,3,1,1,4]
print(canJump(nums))