def rank(n):
    print(n)
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    less, more = 0, lottos.count(0)
    
    for i in lottos:
        if win_nums.count(i):
            less += 1
    
    answer = [rank(less+more), rank(less)]
