class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        s = s.replace("-", "").upper()
        
       
        res = []
        while len(s) > k:
            res.append(s[-k:])  
            s = s[:-k]           
        res.append(s)
        
       
        return "-".join(res[::-1])
