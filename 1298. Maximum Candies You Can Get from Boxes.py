import collections


class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes,initialBoxes):

        candy = 0
        newBoxOpened = False
        key = set()

        queue = collections.deque()
        for box in initialBoxes:
            queue.append((box, 0))

        level = 0

        while queue:
            box, curr = queue.popleft()
            if level != curr:
                if newBoxOpened:
                    level = curr
                    newBoxOpened = False
                else:
                    break
            if status[box] or box in key:
                newBoxOpened = True
                print(box, candies[box])
                candy += candies[box]
                for x in containedBoxes[box]:
                    queue.append((x, curr + 1))
                for k in keys[box]:
                    key.add(k)
            else:
                queue.append((box, curr + 1))

        return candy

ob = Solution()
print(ob.maxCandies(status=[1,0,1,0],
                    candies=[7,5,4,100],
                    keys=[[],[],[1],[]],containedBoxes=[[1,2],[3],[],[]],
                    initialBoxes=[0]))