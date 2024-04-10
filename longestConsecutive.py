from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) solution
        # Solution depends on the concept of storing the corresponding length for each element
        nums_dict = {}
        max_length=0
        for item in set(nums):
            # Getting the length of the previous number and the next number (if any of them is not in the list, then its length is zero "irrelevant")
            prev_elem_len = nums_dict.get(item - 1, 0)
            next_elem_len = nums_dict.get(item + 1, 0)
            
            # The default length of any number is 1, we here add 1 to the next_elem_len or prev_elem_len if exist
            item_length = next_elem_len + prev_elem_len + 1
            
            # updating the value of the length of the prev and next numbers of any exists (this keeps track of all numbers that each number has the correct sequence number)
            nums_dict[item - prev_elem_len] = item_length
            nums_dict[item + next_elem_len] = item_length
        
        
            max_length = max(max_length, item_length)


        return max_length

print(Solution().longestConsecutive([1,0,-1]))