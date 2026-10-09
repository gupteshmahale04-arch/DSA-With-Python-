class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}
      
        for i in arr:
            d[i] = d.get(i, 0) + 1
        

        values = list(d.values())
        return len(values) == len(set(values))
