'''
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.

Examples

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
'''

# arr = [2, 3, 10, 2, 4, 8, 1]
# arr = [4, 3, 2, 1]
arr = [7, 9, 5, 6, 3, 2]
# print(arr)

# 심플하고 arr 이 작으면 문제 없는 코드
max_diff_value = -1
for i, value in enumerate(arr):
    if i == 0:
        continue
    for p in range(i-1, -1, -1):
        diff = value - arr[p]
        # print(f'value: {value}, p: {p}, diff: {diff}')
        if diff > max_diff_value:
            max_diff_value = diff

print(f'max diff is {max_diff_value}')

# arr 이 크면?
import numpy as np
from tqdm import tqdm

#arr = np.random.randint(1000000, size=2*100000)
arr = np.random.randint(10, size=10000)
# arr = [7, 9, 5, 6, 3, 2]
# print(arr)
print('random array ready')

#  아래처럼 기존 방식대로 구현하면, 복잡도는 O(n^2) .. performance test 에서 FAIL
max_diff_value = -1
for i, value in enumerate(tqdm(arr)):
    if i == 0:
        continue
    for p in range(i-1, -1, -1):
        diff = value - arr[p]
        # print(f'value: {value}, p: {p}, diff: {diff}')
        if diff > max_diff_value:
            max_diff_value = diff

print(f'1st case - max diff is {max_diff_value}')

#  아래처럼 max_diff_value 와 min_value 를 keep 하는 방식으로 구현하면, 복잡도는 O(n) .. performance test 에서 OK
max_diff_value = -1000001
min_value = arr[0]
for i, value in enumerate(tqdm(arr)):
    if i == 0:
        continue
    diff = value - min_value
    if diff > 0 and diff > max_diff_value:
        max_diff_value = diff
    if min_value > value:
        min_value = value

print(f'2nd case - max diff is {max_diff_value}')