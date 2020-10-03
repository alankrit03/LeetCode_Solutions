class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(x) for x in version1.split('.')]
        version2 = [int(x) for x in version2.split('.')]

        version1 = version1[::-1]
        version2 = version2[::-1]

        while version1 or version2:
            if version1:
                t1 = version1.pop()
            else:
                t1 = 0

            if version2:
                t2 = version2.pop()
            else:
                t2 = 0

            if t1 > t2:
                return 1
            elif t2 > t1:
                return -1

        else:
            return 0