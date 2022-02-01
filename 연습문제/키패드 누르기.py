def calc(now, number):
    return int(abs(now - number) / 3) + (abs(now - number) % 3)

def check(hand, left_now, right_now, number):
    if number == 0:
        number = 11
        
    if number in [1, 4, 7]:
        return 'L', number, right_now
    elif number in [3, 6, 9]:
        return 'R', left_now, number
    else:
        if calc(left_now, number) < calc(right_now, number):
            return 'L', number, right_now
        elif calc(left_now, number) > calc(right_now, number):
            return 'R', left_now,  number
        else:
            if hand == 'right':
                return 'R', left_now, number
            else:
                return 'L', number, right_now

def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    
    for i in numbers:
        number, left, right = check(hand, left, right, i)
        answer += number
    
    return answer
