def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        if len(stack) == 0:
            stack.append([prices[i], i])
        else:
            while len(stack) > 0 and stack[-1][0] > prices[i]:
                p, idx = stack.pop()
                answer[idx] = i - idx
            stack.append([prices[i], i])
    for p, idx in stack:
        answer[idx] = len(prices) - idx - 1
    return answer