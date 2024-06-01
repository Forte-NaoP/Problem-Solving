from collections import defaultdict
import heapq

push = heapq.heappush
pop = heapq.heappop

class LFUCache:

    def __init__(self, capacity: int):
        self.mem = dict()
        self.recent = []
        self.used = defaultdict(lambda : [0, 0])
        self.capacity = capacity
        self.timer = 0


    def get(self, key: int) -> int:
        self.timer += 1
        if self.mem.get(key) is None:
            return -1
        
        self.used[key][0] += 1
        self.used[key][1] = self.timer
        push(self.recent, (self.used[key][0], self.used[key][1], key))
        return self.mem[key]
        

    def put(self, key: int, value: int) -> None:
        self.timer += 1
        if key not in self.mem.keys() and len(self.mem.keys()) >= self.capacity:
            while self.recent and (self.used[self.recent[0][2]][0] != self.recent[0][0] or 
                                    self.used[self.recent[0][2]][1] != self.recent[0][1]):
                pop(self.recent)
            if self.recent:
                _, _, removed_key = pop(self.recent)
                del self.used[removed_key]
                del self.mem[removed_key]
        self.mem[key] = value
        self.used[key][0] += 1
        self.used[key][1] = self.timer
        push(self.recent, (self.used[key][0], self.used[key][1], key))
        return 


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)