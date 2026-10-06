class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []
        n = len(s)
        start = 0

        for i in range(1, n+1):
            
            if i == n or s[i] != s[i-1]:
                if i - start >= 3:
                    res.append([start, i-1])
                start = i
        return res
