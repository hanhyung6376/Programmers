def solution(clothes):
    answer = 1
    arr1 = [i[1] for i in clothes]
    arr2 = []
    for i in range(len(clothes)):
        if clothes[i][1] not in arr2:
            arr2.append(clothes[i][1])
    for i in arr2:
        answer *= (arr1.count(i) + 1)
    print(arr2)
    print(arr1)

    return answer - 1