class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n):
            prefix = len(set(nums[:i+1]))
            suffix = len(set(nums[i+1:]))
            ans.append(prefix - suffix)

        return ans 