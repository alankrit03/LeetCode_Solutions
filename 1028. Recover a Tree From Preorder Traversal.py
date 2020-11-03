# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        print(S.find('-', 2))

        if not S:
            return None


        temp = ''
        count = 0
        start = 0
        for x in S:
            if x=='-':
                start = 1
                count+=1
            else:
                if start:
                    temp+='- '+str(count)+' -'
                    start=0
                    count=0
                temp+=x
        S = temp

        def findVal(s):
            temp = ''
            for x in s:
                if x == '-':
                    break
                temp += x
            return int(temp)

        def recur(S, level):
            if len(S) < 1:
                return None
            root = TreeNode(findVal(S))
            pat = '- ' +str(level)+ ' -'
            left = S.find(pat)

            addon = 4+len(str(level))
            if left > 0:
                right = S.find(pat, left + 1)
                if right > 0:
                    root.left = recur(S[left + addon:right], level + 1)
                    root.right = recur(S[right + addon:], level + 1)
                else:
                    root.left = recur(S[left + addon:], level + 1)

            return root

        root = recur(S, 1)
        return root

ob = Solution()
ans = ob.recoverFromPreorder('1-2--3--4-5--6--7')