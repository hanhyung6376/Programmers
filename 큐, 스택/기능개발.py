import math
def solution(progresses, speeds):
    answer = []
    job = []
    stack = []
    for p, s in zip(progresses, speeds):
        job_time = math.ceil((100 - p) / s)
        job.append(job_time)

    for i in range(len(job)):
        if len(stack) == 0 or stack[0] >= job[i]:
            stack.append(job[i])
        elif stack[0] < job[i]:
            answer.append(len(stack))
            stack = [job[i]]
    if len(stack) != 0:
        answer.append(len(stack))

    return answer