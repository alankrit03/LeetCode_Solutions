class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        cache = {i for i in range(len(rooms))}

        def checkIn(room):
            if room not in cache:
                return
            cache.remove(room)

            for x in rooms[room]:
                checkIn(x)

        checkIn(0)
        return not cache