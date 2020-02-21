class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for x in s:
            if x.isalnum():
                new_s += x.lower()

        if new_s == new_s[::-1]:
            return True
        return None
        print(new_s)