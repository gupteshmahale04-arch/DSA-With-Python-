class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = [float('inf')] * 26

        for word in words:
            temp = [0] * 26

            for ch in word:
                temp[ord(ch) - ord('a')] += 1

            for i in range(26):
                freq[i] = min(freq[i], temp[i])

        ans = []

        for i in range(26):
            ans.extend([chr(i + ord('a'))] * freq[i])

        return ans