# Let's rewrite the code to make the conditionals clearer

class Solution:
    def maxScore(self, nums1, nums2, k):
        import heapq

        # Create pairs and sort them by the second element in descending order
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: -x[1])

        # Create a min-heap for top k elements
        top_k_elements = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_elements)
        heapq.heapify(top_k_elements)

        # Calculate the initial score
        score = top_k_sum * pairs[k - 1][1]

        # Iterate over the rest of the elements
        for i in range(k, len(nums1)):
            # Remove the smallest element from the top k elements
            smallest_element = heapq.heappop(top_k_elements)
            top_k_sum -= smallest_element

            # Add the next element from the pairs to the top k elements
            next_element = pairs[i][0]
            top_k_sum += next_element
            heapq.heappush(top_k_elements, next_element)

            # Update the score if it's higher than the current score
            potential_score = top_k_sum * pairs[i][1]
            if potential_score > score:
                score = potential_score

        return score



            

nums1 = [2, 7, 9, 8, 3]
nums2 = [5, 1, 3, 4, 2]
k = 3
print(Solution().maxScore(nums1, nums2, 3))