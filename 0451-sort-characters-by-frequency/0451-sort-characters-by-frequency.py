class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
       
        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        buckets = [[] for _ in range(len(s) + 1)]
        for char, freq in d.items():
            buckets[freq].append(char)

        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)
        
        return "".join(result)
