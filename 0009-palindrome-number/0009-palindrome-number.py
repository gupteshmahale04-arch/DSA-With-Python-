class Solution:
    def isPalindrome(self, x: int) -> bool:
        X=str(x)
        count=0
        while len(X)//2!=count:
            if X[count]!=X[len(X)-count-1] :
                return False
            count+=1
        return True 


        