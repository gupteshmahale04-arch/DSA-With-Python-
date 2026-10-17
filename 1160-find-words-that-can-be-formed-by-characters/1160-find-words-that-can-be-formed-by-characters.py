from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        ans = 0

        for word in words:
            word_count = Counter(word)

            good = True
            for ch in word_count:
                if word_count[ch] > chars_count[ch]:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans