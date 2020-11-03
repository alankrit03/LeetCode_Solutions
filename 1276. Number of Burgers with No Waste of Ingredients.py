class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 or 2 * cheeseSlices > tomatoSlices or tomatoSlices > 4 * cheeseSlices:
            return []

        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]

        double = 2 * cheeseSlices
        jumbo = (tomatoSlices - double) // 2
        return [jumbo, cheeseSlices - jumbo]