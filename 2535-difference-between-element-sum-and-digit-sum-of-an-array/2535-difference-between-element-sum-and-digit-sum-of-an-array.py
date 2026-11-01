class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        E_sum=sum(nums)
        D_sum=0
        for i in nums:
           
            if i>9:
                while i!=0:
                    d=i%10
                    D_sum+=d
                    i=i//10

            else:
                D_sum+=i

        return abs(E_sum - D_sum)
        