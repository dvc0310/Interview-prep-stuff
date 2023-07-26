# Let's rewrite the code to make the conditionals clearer

class Solution:
    def totalCost(self, costs, k, candidates):
        import heapq

        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]

        heapq.heapify(head_workers)
        heapq.heapify(tail_workers)

        total_cost = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            # Conditions to decide from which heap to pop
            tail_empty = not tail_workers
            head_empty = not head_workers
            head_is_cheaper = head_workers[0] <= tail_workers[0]

            if tail_empty or (not head_empty and head_is_cheaper):
                total_cost += heapq.heappop(head_workers)

                # Check if there are workers outside the two queues
                if next_head <= next_tail:
                    heapq.heappush(head_workers, costs[next_head])
                    next_head += 1
            elif not tail_empty and not head_is_cheaper:
                total_cost += heapq.heappop(tail_workers)

                # Check if there are workers outside the two queues
                if next_head <= next_tail:
                    heapq.heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return total_cost

# Test the function
solution = Solution()
costs = [17,12,10,2,7,2,11,20,84,3,1,4,9,5,89]
k = 3
candidates = 4
print(solution.totalCost(costs, k, candidates))