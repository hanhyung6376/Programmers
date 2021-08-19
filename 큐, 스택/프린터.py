from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque()
    priorities = deque(priorities)
    for i in range(len(priorities)):
        queue.append([priorities[i], i])

    while True:
        if queue[0][0] == max(priorities):
            check, idx = queue.popleft()
            priorities.popleft()
            answer.append(idx)
            if location == idx:
                return len(answer)
        else:
            queue.rotate(-1)
            priorities.rotate(-1)