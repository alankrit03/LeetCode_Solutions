class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        n = (len(arr)+1)//2
        ans = 0
        for _,f in c.most_common():
            n -= f
            ans += 1
            if n<=0:
                return ans