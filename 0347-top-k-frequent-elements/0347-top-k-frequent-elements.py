class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

      
        keys = list(d.keys())
        values = list(d.values())

       
        res = []
        for _ in range(k):
          
            max_index = 0
            for i in range(1, len(values)):
                if values[i] > values[max_index]:
                    max_index = i
          
            res.append(keys[max_index])
           
            values[max_index] = -1
        return res
