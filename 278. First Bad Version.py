# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 0, n

        while h - l > 1:
            m = (h + l) // 2

            if not isBadVersion(m):
                l = m
            else:
                h = m

        return h