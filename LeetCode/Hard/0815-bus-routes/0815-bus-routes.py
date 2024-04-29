from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_dict = defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_dict[stop].append(bus)
        visit_bus = set()
        visit_stop = set()
        q = deque()

        q.append((source, 1))
        visit_stop.add(source)
        for bus in stop_dict[source]:
            visit_bus.add(bus)
            for stop in routes[bus]:
                if stop != source:
                    q.append((stop, 1))
                    visit_stop.add(stop)
        
        while q:
            cur, num = q.popleft()
            if cur == target:
                return num
            for bus in stop_dict[cur]:
                if bus in visit_bus:
                    continue
                visit_bus.add(bus)
                for stop in routes[bus]:
                    if stop in visit_stop:
                        continue
                    q.append((stop, num + 1))
                    visit_stop.add(stop)
        return -1