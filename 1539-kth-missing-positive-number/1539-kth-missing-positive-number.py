class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        L,R=0,len(arr)-1
        while L<=R:
            M=(L+R)//2
            Missing=arr[M]-(M+1)
            if Missing<k:
                L=M+1
            else:
                R=M-1
        return L+k

    
        