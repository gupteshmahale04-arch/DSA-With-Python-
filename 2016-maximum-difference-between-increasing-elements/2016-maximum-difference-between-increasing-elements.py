class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        min_num = nums[0]
        ans = -1

        for i in range(1, len(nums)):
            if nums[i] > min_num:
                ans = max(ans, nums[i] - min_num)
            else:
                min_num = nums[i]

        return ans


        
        