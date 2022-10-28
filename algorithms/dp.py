"""
1. Define status
2. Find recurrence relation
3. Calculate O(N)
4. Do programming

방법론
1. Top-Down (by recurrence relation)
2. Bottom-Up (by iteration loop) => python에서 재귀 함수 알고리즘은 시간복잡도에서 불리할 수 있다.
"""

# 2차원 배열을 이용한 기본 풀이
A = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
N: int = len(A)
DP = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(i + 1):
        DP[i][j] = max(DP[i - 1][j - 1], DP[i - 1][j]) + A[i][j]

for row in DP:
    print(row)

# 어느 미친 사람의 완벽한 솔루션
solution = (
    lambda t, l=[]: max(l)
    if not t
    else solution(t[1:], [max(x, y) + z for x, y, z in zip([0] + l, l + [0], t[0])])
)
