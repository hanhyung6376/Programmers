from collections import defaultdict

def solution(tickets):
    dict = defaultdict(list)
    for i, j in tickets:
        dict[i].append(j)

    for i in dict:
        dict[i].sort()
    answer = dfs(dict)

    return answer


def dfs(dict):
    stack = ["ICN"]
    route = []
    while stack:
        top = stack[-1]
        if top not in dict or len(dict[top]) == 0:
            route.append(stack.pop())
        else:
            stack.append(dict[top].pop(0))
    return route[::-1]