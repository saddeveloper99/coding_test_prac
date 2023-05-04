'''
https://school.programmers.co.kr/learn/courses/30/lessons/70128
내적

문제 설명

길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. 
a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.

이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다.
(n은 a, b의 길이)


제한사항

a, b의 길이는 1 이상 1,000 이하입니다.
a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

'''

a = [1,2,3,4]
b = [-3,-1,0,2]	
# 3

'''
1. 구해야 하는 것
    # a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]
2. 1을 구하기 위해 필요한 것
    # 배열의 길이 
        # len()
    # for문
'''

# 풀이
answer = 0
for i in range(len(a)):
    answer += a[i]*b[i]
print(answer)


# 제출용 함수
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer


# 
def solution(a, b):
    return sum([a[i]*b[i] for i in range(len(a))])

print(solution(a,b))


# zip으로 묶기?
print(list(zip(a, b)))