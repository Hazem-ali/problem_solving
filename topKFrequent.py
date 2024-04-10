from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        ans = []
        for num in nums:
            nums_dict[num] = nums_dict.get(num, 0) + 1
            
        sorted_nums = sorted(nums_dict.items(), key=lambda x: x[1], reverse=True)
        
        for i in range(k):
            ans.append(sorted_nums[i][0])
        
        return ans
    
print(Solution().topKFrequent([1,2],2))
