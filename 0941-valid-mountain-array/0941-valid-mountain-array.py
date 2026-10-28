class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        # c=0
        # for i in range (1,len(arr)):
            
        #     if arr[i-1]==arr[i] or len(arr)<3:
        #         return False
        #     elif arr[i-1]>arr[i]:
        #         pass
        #     else:
        #         c+=1
        # return c==1
        n=len(arr)
       

        if n<3:
            return False
        i=0
        while i+1<n and arr[i]<arr[i+1]:
            i+=1

        if i ==0 or i==n-1:
            return False

        while i+1<n and arr[i]>arr[i+1]:
            i+=1
        return i==n-1       
        
        
        