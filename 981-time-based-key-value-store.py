class TimeMap:
    def __init__(self):
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        currArr = self.dict[key]
        low, high = 0, len(currArr)

        while low < high:
            mid = low + (high - low) // 2
            if currArr[mid][0] > timestamp:
                high = mid
            else:
                low = mid + 1
        
        if high == 0:
            return ""
        else:
            return currArr[high - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
