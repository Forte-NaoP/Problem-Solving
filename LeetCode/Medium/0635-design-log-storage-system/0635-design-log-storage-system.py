APPROX = {
    'Year' : 10 ** 10,
    'Month' : 10 ** 8,
    'Day' : 10 ** 6,
    'Hour' : 10 ** 4,
    'Minute' : 10 ** 2,
    'Second' : 10 ** 0,
}

class LogSystem:

    def __init__(self):
        self.ts = set()

    def put(self, id: int, timestamp: str) -> None:
        ts = int(timestamp.replace(':', ''))
        self.ts.add((ts, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        coeff = APPROX[granularity]
        def cut(val):
            return val // coeff * coeff
        
        start = cut(int(start.replace(':', '')))
        end = cut(int(end.replace(':', '')))
        
        ts_list = sorted(self.ts, key=lambda x: x[0])

        def lower_bound(x):
            lo, hi = 0, len(ts_list)

            while lo < hi:
                mid = (lo + hi) // 2
                mid_ts = cut(ts_list[mid][0])
                if mid_ts < x:
                    lo = mid + 1
                else:
                    hi = mid
            return hi
        
        lb = lower_bound(start)

        ans = []
        while lb < len(ts_list) and cut(ts_list[lb][0]) <= end:
            ans.append(ts_list[lb][1])
            lb += 1

        return ans