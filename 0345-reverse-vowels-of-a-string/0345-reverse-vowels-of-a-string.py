class Solution:
    def reverseVowels(self, s: str) -> str:
        V=set("AEIOUaeiou")
        L=list(s)
        l,r=0,len(L)-1
        while l<r:
            while l<r and L[l]not in V:
                l+=1
            while l<r and L[r]not in V:
                r-=1
            L[l],L[r]=L[r],L[l]
            l+=1
            r-=1
        return "".join(L)

