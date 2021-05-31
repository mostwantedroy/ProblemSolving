from collections import defaultdict
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = defaultdict(int)

        for num in nums:
            hash_map[num] += 1

        heap = []

        for key in hash_map:
            heapq.heappush(heap, (hash_map[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        answer = []

        for item in heap:
            answer.append(item[1])

        return answer