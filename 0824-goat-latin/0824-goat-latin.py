class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []

        for i, word in enumerate(words, start=1):
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            
            # Add 'a' * i at the end
            goat_word += "a" * i
            result.append(goat_word)
        
        return " ".join(result)
