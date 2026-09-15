class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count=0
        Op=[]
        for i in range (len(nums)):
            
            count+=nums[i]
            Op.append(count)
        return Op
