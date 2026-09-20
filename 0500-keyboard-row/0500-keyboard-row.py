class Solution:
    def findWords(self, words: list[str]) -> list[str]:  
        l1=set("qwertyuiopQWERTYUIOP")
        l2=set("asdfghjklASDFGHJKL")
        l3=set("zxcvbnmZXCVBNM")
        ans=[]
       
        for i in words:
            C1=C2=C3=0
            for j in i:
            
                if j in l1:
                    C1+=1
                elif j in l2:
                    C2+=1
                elif j in l3:
                    C3+=1

            if len(i)==C1 or  len(i)==C2 or  len(i)==C3:
                    ans.append(i)

        return ans