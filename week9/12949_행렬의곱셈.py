'''
https://school.programmers.co.kr/learn/courses/30/lessons/12949
행렬의 곱셈

문제 설명

2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, 
solution을 완성해주세요.


제한 조건

행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.


입출력 예

arr1
[[1, 4], [3, 2], [4, 1]]	
arr2
[[3, 3], [3, 3]]	
return		
[[15, 15], [15, 15], [15, 15]]

arr1
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	
arr2
[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	
return		
[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''
from sys import path
path.append("../codingtest_prac")
from timecheckers.timechecker import elapsed
'''
1. 구해야 하는 것
    행렬의 곱
2. 1을 구하기 위해 필요한 것
    분명히 numpy에 있는 기능일 것.
    행렬을 다룰땐 zip을 쓰면 좋다.
    일단 그냥 해보기
3. 그 외 고려해야 할 사항
'''
arr1 = [[2, 3, 2], 
        [4, 2, 4], 
        [3, 1, 4]]
arr2 = [[5, 4, 3], 
        [2, 4, 1], 
        [3, 1, 1]]

# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]


# answer = []
# for i in range(len(arr1)):
#     row = []
#     for j in range(len(arr2[0])):
#         a = 0
#         for k in range(len(arr2)):
#             a += arr1[i][k] * arr2[k][j]
#         row.append(a)
#     answer.append(row)
# print(answer)


@elapsed
def solution(arr1,arr2):
    answer = []
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            a = 0
            for k in range(len(arr2)):
                a += arr1[i][k] * arr2[k][j]
            row.append(a)
        answer.append(row)
    return answer


import numpy as np
@elapsed
def solution2(arr1, arr2): 
    return (np.array(arr1) @ np.array(arr2)).tolist()

print(solution(arr1,arr2))
print(solution2(arr1,arr2)) # 길이가 길어질 수록 넘파이가 빠름

def solution(arr1, arr2):
    return [[sum(a*b for a, b in zip(row1, col1)) for col1 in zip(*arr2)] for row1 in arr1]