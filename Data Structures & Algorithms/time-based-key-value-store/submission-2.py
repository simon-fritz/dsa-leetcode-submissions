class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        times = self.store[key]
        l,r = 0,len(times)-1
        res=""
        while l<=r:
            m = l+((r-l)//2)
            if times[m][0] == timestamp:
                return times[m][1]
            elif times[m][0] > timestamp:
                r = m-1
            else:
                res = times[m][1]
                l = m+1
        return res