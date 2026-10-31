class Solution:
    def isFascinating(self, n: int) -> bool:
       A=str(n)+str( n*2)+str(n*3)
       return len(A) == 9 and set(A) == set("123456789")

        
        