def solution(s):
    answer = ''
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_dict = {}
    for i in range(10):
        num_dict[number[i]] = i
    check = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            check += i
            if check in num_dict.keys():
                answer += str(num_dict[check])
                check = ''

    return int(answer)