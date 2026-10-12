class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        mod_counts = [0] * k
        mod_counts[0] = 1
        
        running_sum = 0
        total_subarrays = 0
        
        for num in nums:
            running_sum += num
            
            rem = running_sum % k
            
            total_subarrays += mod_counts[rem]

            mod_counts[rem] += 1
            
        return total_subarrays