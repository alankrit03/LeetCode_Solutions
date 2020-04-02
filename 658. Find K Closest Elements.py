class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        if not arr or not k:
            return []

        def start_point():
            l, h = 0, len(arr)

            while h - l > 1:
                m = (h + l) // 2

                if arr[m] > x:
                    h = m
                else:
                    l = m
            if l < n - 1:
                if x - arr[l] > arr[l + 1] - x:
                    return l + 1
            return l

        left = start_point()
        ans = [arr[left]]

        right = left + 1
        left -= 1
        k -= 1

        while k:
            if left > -1 and right < n:
                if x - arr[left] <= arr[right] - x:
                    ans.insert(0, arr[left])
                    left -= 1
                else:
                    ans.append(arr[right])
                    right += 1

            elif left > -1:
                ans.insert(0, arr[left])
                left -= 1
            else:
                ans.append(arr[right])
                right += 1

            k -= 1

        return ans