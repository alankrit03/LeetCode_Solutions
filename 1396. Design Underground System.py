class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.averagetime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_record = self.checkin[id]
        temp_key = checkin_record[0] + ':' + stationName

        if self.averagetime.get(temp_key):
            prev = self.averagetime[temp_key][0]
            travel_times = self.averagetime[temp_key][1]
            temp = ((prev * travel_times) + (t - checkin_record[1])) / (travel_times + 1)
            self.averagetime[temp_key] = [temp, travel_times + 1]

        else:
            self.averagetime[temp_key] = [t - checkin_record[1], 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        temp_key = startStation + ":" + endStation
        return self.averagetime[temp_key][0]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)