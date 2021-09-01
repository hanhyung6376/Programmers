def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1]
        if a == b[0:len(a)]:
            return False
    return answer