def solution(n):
    dp = [0] * n
    dp[0:3] = [1, 1, 2, 3]
    if n >3:
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n] % 1000000007