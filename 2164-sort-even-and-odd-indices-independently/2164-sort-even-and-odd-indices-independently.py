class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        num=[]
        even_index=[]
        odd_index=[]
        for i in range(len(nums)):
            if i %2==0:
                even_index.append(nums [i])
            else:
                odd_index.append(nums [i])
        even_index.sort()
        odd_index.sort(reverse=True)
        even=0
        odd=0
        for i in range(len(nums)):
            if i %2==0:
                num.append(even_index[even])
                even+=1
            else:
                num.append(odd_index[odd])
                odd+=1
        return num