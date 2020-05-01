class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        def merge(L, R):
            len_L = len(L)
            len_R = len(R)
            arr = []
            for _ in range(len_L + len_R):
                if L and R:
                    if L[0] >= R[0]:
                        arr.append(R.pop(0))
                    else:
                        arr.append(L.pop(0))
                else:
                    if L:
                        arr.extend(L)
                    else:
                        arr.extend(R)
                    break

            return arr

        n = len(arr)
        if n > 1:
            L = self.sortArray(arr[:n // 2])
            R = self.sortArray(arr[n // 2:])
            arr = merge(L, R)
        return arr



