'''
2 x N 크기의 구역을
2 x 1 이나 2 x 2 크기의 타일을 사용해서, 채울 수 있는 경우의 수를 구해보자.
단, 실제 경우의 수는 너무 많을 수 있으므로 구한 경우의 수를 주어진 M 으로 나눈 나머지만 출력하자.

예)
2 x 8 크기의 구역에 대해서.. 주어진 100으로 나눈 나머지는 71 이 나온다.

힌트
전체 영역이 2 x 3 인 경우는 2 x 2 인 경우와, 2 x 1 인 경우를 합하면 구할 수 있으며
2 x 1 인 경우가 왼쪽에 올 수 있는 경우와 오른쪽에 올 수 있는 경우로 나눌 수 있다. 즉, 2 x 1 영역의 경우를 2배 해 주면 된다.

그러므로
2 x 3 의 경우 2x2 인 경우 3 + 2x1 인 경우 1*2 = 5
2 x 4 의 경우 (위에꺼까지 해서 5가 2x2 에 해당하는 거고, 3이 2x1에 해당한다) 그러므로, 5 + 3*2 = 11
2 x 5 의 경우는 11 + 5*2 = 21
...
'''

def Solution(N, M):
    if N == 1:          # N이 1이면 경우의 수는 1
        return 1 % M
    elif N == 2:        # N이 2이면 경우의 수는 3
        return 3 % M
    else:               # N이 3 이상이면 로직이 필요
        local_sum_1 = 1     # 2x1 의 경우
        local_sum_2 = 3     # 2x2 의 경우
        local_sum_all = 0

        for i in range(2, N, 1):
            local_sum_tmp = (local_sum_2 + local_sum_1 * 2) % M
            local_sum_1 = local_sum_2
            local_sum_2 = local_sum_tmp
            #
            local_sum_all = local_sum_tmp

            print(f'local sum #1: {local_sum_1}, #2: {local_sum_2}, #tmp: {local_sum_tmp}')
        return local_sum_all

print(Solution(3, 100))  # 5
print(Solution(4, 100))  # 11
print(Solution(5, 100))  # 11
print(Solution(8, 100))  # 71
'''
local sum #1: 3, #2: 5, #tmp: 5
5
local sum #1: 3, #2: 5, #tmp: 5
local sum #1: 5, #2: 11, #tmp: 11
11
local sum #1: 3, #2: 5, #tmp: 5
local sum #1: 5, #2: 11, #tmp: 11
local sum #1: 11, #2: 21, #tmp: 21
21
local sum #1: 3, #2: 5, #tmp: 5
local sum #1: 5, #2: 11, #tmp: 11
local sum #1: 11, #2: 21, #tmp: 21
local sum #1: 21, #2: 43, #tmp: 43
local sum #1: 43, #2: 85, #tmp: 85
local sum #1: 85, #2: 71, #tmp: 71
71
'''
