from heapq import heappush, heappop
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for i in range(k - 1):
            heappush(heap, (-nums[i], i))
        for i in range(k - 1, len(nums)):
            heappush(heap, (-nums[i], i))
            while heap[0][1] + k - 1 < i:
                heappop(heap)
            result.append(-heap[0][0])
        return result
