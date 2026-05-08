from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] +=1
        num_dict = dict(sorted(num_dict.items(), key=lambda x: x[1], reverse=True))
        return list(num_dict.keys())[:k]

        
