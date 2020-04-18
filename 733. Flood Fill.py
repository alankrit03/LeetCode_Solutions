import sys

sys.setrecursionlimit(10 ** 7)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        present_color = image[sr][sc]
        if newColor == present_color:
            return image
        m = len(image)
        n = len(image[0])

        def recur_color(i, j, image):
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != present_color:
                return

            image[i][j] = newColor
            recur_color(i + 1, j, image)
            recur_color(i - 1, j, image)
            recur_color(i, j + 1, image)
            recur_color(i, j - 1, image)

        recur_color(sr, sc, image)

        return image