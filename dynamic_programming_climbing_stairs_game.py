'''
계단 오르기는 계단 아래 시작점부터 계단 꼭대기 도착점까지 가장 계단을 적게 밟고 올라가는 게임이다.
예를 들어
10(시작) 20 15 25 10 20(도착)
으로 계단이 있을 때
10(시작) 20 25 20(도착)
이렇게 밟았다면 총 점수는 10 + 20 + 25 + 20 = 75 점이 된다.

다음과 같은 3가지 규칙이 있다.
- 계단은 한번에 1개 또는 2개의 계단을 오를 수 있다. 즉, 계단 하나를 밟으면 이어서 다음 계단이나 다음 다음 계단으로 오를 수 있다.
- 한꺼번에 2개의 계단을 오를 때는 중간 계단을 밟아서는 안된다. 단 시작점은 계단에 포함되지 않는다.
- 마지막 도착 계단은 반드시 밟아야 한다.

각 계단에 적혀 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 점수의 최대값을 구하는 프로그램을 작성해보자.

sample
10 20 15 25 10 20 -> 75
13 1 15 27 29 21 20 -> 96
'''

# 따라서 단순히 이전 계단들의 누적된 값에 현재 계단의 점수를 더하는 것이 아니라
# 현재 계단에서 이전 계단을 밟고 왔는지 그렇지 않은지의 경우를 비교해서 더 높은 점수인 경우를 선택해야 한다.

#list_steps = [10, 20, 15, 25, 10, 20]
list_steps = [13, 1, 15, 27, 29, 21, 20]
list_steps = [0] + list_steps               # 0번째 계단이 있어야 하므로 [0]을 앞에 추가한다.
solution_steps = [0] * len(list_steps)

# 처음부터 두 번째 계단까지 값을 구함
solution_steps[0] = 0
solution_steps[1] = list_steps[1]
solution_steps[2] = list_steps[1] + list_steps[2]

# 세번째 계단 부터 누적값을 계산함
for i in range(3, len(list_steps), 1):
    no_jump_steps = list_steps[i] + list_steps[i-1] + solution_steps[i-3]
    one_jump_steps = list_steps[i] + solution_steps[i-2]

    # 둘 중 큰 값을 선택
    if no_jump_steps > one_jump_steps:
        solution_steps[i] = no_jump_steps
    else:
        solution_steps[i] = one_jump_steps

    print(f'solution_steps[{i}] : {solution_steps[i]}')

print(solution_steps[len(list_steps)-1])

print(solution_steps)
'''
solution_steps[3] : 28
solution_steps[4] : 55
solution_steps[5] : 70
solution_steps[6] : 78
solution_steps[7] : 96
96
[0, 13, 14, 28, 55, 70, 78, 96]
'''
