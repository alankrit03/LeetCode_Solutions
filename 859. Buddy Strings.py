class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        n = len(A)
        if n != len(B):
            return False

        first = second = None
        for i in range(n):
            if A[i] != B[i]:
                if second:
                    return False
                if first is not None:
                    second = i
                else:
                    first = i

        # print(first,second)
        # print(A[first],B[second])
        if first is not None and second:
            return (A[first] == B[second] and A[second] == B[first])
        elif first:
            return False
        else:
            cache = set()
            for x in A:
                if x in cache:
                    return True
                cache.add(x)

        return False