class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        Sum=nums[0]
        ans=nums[0]
        for i in range (1,len(nums)):
            if nums[i-1]<nums[i]:
                Sum+=nums[i]
            else:
                ans=max(ans,Sum)
                Sum=nums[i]
        return max(ans,Sum)