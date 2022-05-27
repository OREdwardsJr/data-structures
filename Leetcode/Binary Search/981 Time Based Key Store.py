class TimeMap:

    def __init__(self):
        self.table = {
            "": {}
        }

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key] = {timestamp: value}

    '''
    def get(self, key: str, timestamp: int) -> str:
        last_item = list(self.table[key].keys())[-1]
        self.table[key][timestamp] = self.table[key].get(timestamp, self.table[key][last_item])
        return self.table[key][timestamp]
    '''   

    def get(self, key: str, timestamp: int) -> str:
        last_item = sorted(list(self.table[key].keys()))[-1]
        self.table[key][timestamp] = self.table[key].get(timestamp, self.table[key][last_item])
        return self.table[key][timestamp] if timestamp >= last_item else ""