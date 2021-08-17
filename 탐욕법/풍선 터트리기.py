def solution(a):
    answer = [0] * len(a)
    front, rear = float('inf'), float('inf')
    for i in range(len(a)):
        if a[i] < front:
            front= a[i]
            answer[i] = 1
        if a[-1-i] < rear:
            rear = a[-1-i]
            answer[-1-i] = 1
    return sum(answer)