class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
     
        seen_rem = {0: -1}
        
        running_sum = 0
        
        for i, num in enumerate(nums):
            running_sum += num
            rem = running_sum % k
            
            if rem in seen_rem:
             
                if i - seen_rem[rem] >= 2:
                    return True
            else:
               
                seen_rem[rem] = i
                
        return False