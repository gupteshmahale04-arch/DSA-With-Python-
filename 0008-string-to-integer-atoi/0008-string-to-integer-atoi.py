class Solution:
    def myAtoi(self, s: str) -> int:
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        
        while i < n and s[i] == " ":
            i += 1
        
     
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1
        
    
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord("0")  
            result = result * 10 + digit
            i += 1
            
            if sign * result <= INT_MIN:
                return INT_MIN
            if sign * result >= INT_MAX:
                return INT_MAX
        
        return sign * result
