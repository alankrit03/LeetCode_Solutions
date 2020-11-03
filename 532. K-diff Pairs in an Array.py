"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
So I suppose you would have thought of a basic solution where we traverse over the array
and keep checking if (x+k) or x-k is present in our hashmap or not ,
increasing our 'ans' accordingly and then add our current element
to the hashmap or hashset (call it whatever you want).

You are surely stuck at the point where How to check whether a pair has already been counted in our 'ans' or not.

Surely adding the pairs in hashset will consume a lot of memory and is pretty heavy implementation actually.

Think about the Sum of the two elements in that pair.
Yessss...you got the point right. The sum of the two elements will always be unique for each unique pair.
I would really like you to use a pencil and paper try to validate this urself before getting into the code.
Once you are sure then you just have to keep an extra hashset which keeps
track of the sum of pair of elements that you have counted and thus you get the right ans.

And finaly here is simple and clean Python3 code which gave me a 99.57% better run time according to the leetcode servers.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cache = set()
        added = set()

        ans = 0

        for x in nums:
            prev = x - k
            nex = x + k
            if prev in cache and (x + prev) not in added:
                ans += 1
                added.add(x + prev)
            if nex in cache and (x + nex) not in added:
                ans += 1
                added.add(x + nex)
            cache.add(x)

        return ans