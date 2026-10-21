class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count=0
        num=set(nums)
        for i in  num:
            if i-diff in num and i+diff in num :
                count+=1

        return count


        