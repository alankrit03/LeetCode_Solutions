class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        for i in range(1,len(distance)):
            distance[i] += distance[i-1]
        start , destination = min(start,destination), max(start,destination)
        if start:
            clockwise = distance[destination-1]-distance[start-1]
        else:
            clockwise = distance[destination-1]
        return min(clockwise, distance[-1]-clockwise)