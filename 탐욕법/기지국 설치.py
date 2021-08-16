def solution(n, stations, w):
    answer = 0
    idx = 0
    now = 1
    while now <= n:
        if idx < len(stations) and now >= stations[idx] - w:
            now = stations[idx] + w + 1
            idx += 1
        else:
            now += 2 * w + 1
            answer += 1

    return answer