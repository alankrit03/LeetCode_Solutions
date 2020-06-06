class Solution:
    def checkRecord(self, s: str) -> bool:
        len_s = len(s)

        if len_s < 2:
            return True

        count_absent = 0

        for i in range(len_s - 2):
            if s[i] == 'L':
                if s[i:i + 3] == 'LLL':
                    return False

        if s.count('A') < 2:
            return True
