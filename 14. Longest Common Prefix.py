class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        def is_prefix(id):
            temp = strs[0][:id]
            for x in strs:
                if not x.startswith(temp):
                    return False
            return True

        min_ = 10_000_000
        for x in strs:
            if len(x) < min_:
                min_ = len(x)

        l, h = 0, min_ + 1
        while h - l > 1:
            m = (l + h) // 2

            if is_prefix(m):
                l = m
            else:
                h = m

        return strs[0][:l]