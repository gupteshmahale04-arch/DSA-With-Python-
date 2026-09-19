class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        C=[]
        count=0
        for i in nums:
                if i==1:
                    count+=1
                C.append(count)
                  
                if i==0:
                   
                    count=0
        return max(C)
    
        
        # max_count,count=0,0
        # for i in nums:
        #         if i==1:
        #             count+=1
        #             max_count=max(max_count,count)
                  
        #         if i==0:
                   
        #             count=0
        # return max_count