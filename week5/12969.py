'''
https://school.programmers.co.kr/learn/courses/30/lessons/12969
직사각형 별찍기

문제 설명
이 문제에는 표준 입력으로 두 개의 정수 n과 m이 주어집니다.
별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.


제한사항
n과 m은 각각 1000 이하인 자연수입니다.

입출력 예시
5 3
*****
*****
*****
'''
a, b = map(int, input().strip().split(' '))

arr = ['*'*a]

for i in range(b):
    print("".join(arr))

# 람다 연습
# list(map(lambda i: print("".join(arr)), range(b)))