def solution(n, t, m, timetable):
    answer = ''
    for i, time in enumerate(timetable):
        h, mm = map(int, time.split(":"))
        timetable[i] = h*60 + mm
    
    timetable.sort()
    
    buses = [9*60]
    bus_queue = []
    for i in range(n-1):
        buses.append(buses[-1]+t) # 버스 타임라인
    
    def bound(k, upper):
        lo, hi = -1, len(timetable)
        
        while lo + 1 < hi:    
            mid = (lo+hi) // 2
            if timetable[mid] < k:
                lo = mid
            elif timetable[mid] == k:
                if upper:
                    lo = mid
                else:
                    hi = mid
            else:
                hi = mid
        return hi
    
    for bus in buses:
        bus_queue.append([bound(bus, upper=True), 0, 0, 0]) 
        # [각 버스 도착 후에 줄 선 크루 인덱스, 버스 배차 사이에 대기 중인 크루 수, 현재 버스에 탄 마지막 크루원 인덱스, 버스 탑승 인원]
    
    before_idx = 0
    for i in range(n):
        bus_queue[i][1] = bus_queue[i][0] - before_idx # 버스 배차 사이에 대기 중인 크루 수
        before_idx = bus_queue[i][0]
    
    left = 0
    last_idx = 0
    for i in range(n):
        last_idx += min(left + bus_queue[i][1], m)
        bus_queue[i][2] = last_idx
        bus_queue[i][3] = min(left + bus_queue[i][1], m)
        left = max(0, left + bus_queue[i][1] - m)
    
    if bus_queue[-1][3] < m:
        return f'{(buses[-1]//60):02}:{(buses[-1]%60):02}'
    
    last_time = timetable[bus_queue[-1][2]-1] - 1
    return f'{(last_time//60):02}:{(last_time%60):02}'

        