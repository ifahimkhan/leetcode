class UndergroundSystem:
    def __init__(self):
        self.ids = set()
        self.memo = dict()
        self.avg_time = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.ids: return
        self.ids.add(id)
        self.memo[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.ids: return
        self.ids.remove(id)
        
        start_station, start_time = self.memo[id]
        self.memo.pop(id)
        end_station, end_time = stationName, t
        
        route = (start_station, end_station)
        delta_t = end_time - start_time
        
        average_time, count = self.avg_time.get(route, (0, 0))
        self.avg_time[route] = ((average_time * count + delta_t) / (count + 1), count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg_time[(startStation, endStation)][0]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
