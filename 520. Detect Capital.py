class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)<2:
            return True
        if str.isupper(word) or str.islower(word[1:]):
            return True
        return False