class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}   
        count = 0
        max_len = 0
        
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in count_map:
                max_len = max(max_len, i - count_map[count])
            else:
                count_map[count] = i
            
            i += 1
        
        return max_len
