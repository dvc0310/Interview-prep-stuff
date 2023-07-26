
import random
def three_sum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0: 
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return result



def main():
    A = []
    for i in range (0 ,10):
         A.append (random.randint(-10, 10))
    # Replace 'three_sum' with the name of your function
    
    result = three_sum(A)

    if result:
        print("Triplets with zero sum:")
        print(A)
        for triplet in result:
            print(triplet)
    else:
        print("No triplets found with a sum of zero.")

if __name__ == "__main__":
    main()
