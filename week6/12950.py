'''
https://school.programmers.co.kr/learn/courses/30/lessons/12950
행렬의 덧셈

문제 설명

행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 
같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 
행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건

행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
 
'''
arr1 = [
    [1, 2],
    [2, 3],
    [2, 3],
]
arr2 = [
    [3, 4],
    [5, 6],
    [6, 6],
]
# [[4,6],[7,9],[8,9]]
print(list(zip(arr1, arr2)))
"""
1. 구해야 하는 것
    # 두 행렬의 같은 행, 같은 열의 값을 서로 더한 행렬
2. 1을 구하기 위해 필요한 것
    # 각각의 행과 열의 길이
        # len()
    # 각각 더하는 방법
        # for문
"""

# 풀이
a = len(arr1)  # 3
b = len(arr1[0])  # 2

answer = []
for i in range(a):
    answer.append([])  # 열의 개수 추가하기
    for j in range(b):
        answer[i].append(arr1[i][j] + arr2[i][j])  # 더한 값을 넣기
0.

# 제출용 함수
# def solution(arr1, arr2):
#     a = len(arr1)
#     b = len(arr1[0])
#     answer = []
#     for i in range(a):
#         answer.append([])
#         for j in range(b):
#             answer[i].append(arr1[i][j] + arr2[i][j])
#     return answer

#


def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

##


# def solution(arr1, arr2):
#     answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
#     return answer


print(solution(arr1, arr2))
