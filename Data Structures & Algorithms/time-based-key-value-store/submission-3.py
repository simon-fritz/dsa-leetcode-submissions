class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        stamps = self.store[key]
        low = 0
        high = len(stamps)-1
        res = ""
        while low <= high:
            m = (low + high)//2
            if stamps[m][0] <= timestamp:
                res = stamps[m][1]
                low = m+1
            else:
                high = m-1

        return res
        
