'''
https://school.programmers.co.kr/learn/courses/30/lessons/12940
최대공약수와 최소공배수


문제 설명

두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, 
solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 
그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 
최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 
반환해야 합니다.


제한 사항

두 수는 1이상 1000000이하의 자연수입니다.
'''
n = 3
m = 12
# [3, 12]
'''
1. 구해야 하는 것
    # 최대 공약수와 최소 공배수
2. 1을 구하기 위해 필요한 것
    # n, m의 공약수와 공배수들
        
3. 그 외 고려사항
    # n이 m의 약수 또는 m이 n의 약수일때, 즉시 n,m을 반환
    # n과 m 이 모두 소수면 공약수는 n*m
    # 그 외에는 n*m을 최대 공약수로 나눠주면? 최소공배수 
    # 유클리드 호제법?
'''

answer = []
for i in range(n if n > m else m, 0, -1):
    if n % i == 0 and m % i == 0:
        answer.append(i)
        break
answer.append(n*m//answer[0])

print(answer)


def solution(n, m):
    answer = []
    for i in range(n if n > m else m, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    answer.append(n*m//answer[0])
    return answer
# print(solution())


"""

유클리드 호제법


c  d
108 32
t = 12

c  d
32  12
t = 8

c  d
12  8
t = 4

c d 
8 4 
t = 0

"""

