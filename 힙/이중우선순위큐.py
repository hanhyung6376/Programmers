import heapq
def solution(operations):
    max_heap = []
    min_heap = []
    for i in operations:
        cmd, num = i.split()
        if cmd == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, [-int(num), int(num)])
        elif cmd == 'D':
            if len(max_heap) == 0:
                continue
            if int(num) == 1:
                a, b  = heapq.heappop(max_heap)
                min_heap.remove(b)
            elif int(num) == -1:
                a = heapq.heappop(min_heap)
                max_heap.remove([-a, a])

    if max_heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        return [0, 0]