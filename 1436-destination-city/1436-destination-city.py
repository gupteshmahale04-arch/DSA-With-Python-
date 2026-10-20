class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        start=set()
        for a,b in paths:
            start.add(a)
        
        for a,b in paths:
            if b not in start:
                return b

        