'''
https://school.programmers.co.kr/learn/courses/30/lessons/12924
숫자의 표현

문제 설명
Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 
자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과
 같이 4가지로 표현 할 수 있습니다.

1 + 2 + 3 + 4 + 5 = 15
4 + 5 + 6 = 15
7 + 8 = 15
15 = 15

자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 
return하는 solution를 완성해주세요.

제한사항
n은 10,000 이하의 자연수 입니다.
'''


'''
1. 구해야 하는 것
    n을 연속된 k개의 자연수들의 합으로 표현하는 방법의 수
2. 1을 구하기 위해 필요한 것
    연속된 자연수들을 구할 방법
        하나씩 더하면서 완전탐색하기
    k의 개수 * k의 평균은 n이 되어야한다.

3. 그 외 고려해야 할 사항
'''
from timechecker import elapsed
n = 10000000
# 4


"""
k의 개수는?
n을 k개의 연속된 자연수로 표현하기
m
m + m+1
m + m+1 + m+2
m + m+1 + m+2 + m+3 ...
>> k*m + (k-1)


# answer = 0
# for i in range(1, n+1):
    
# print(answer)
"""




# answer = 0
# for i in range(1, n+1): # 1부터 n까지
#     sum = 0 # n과 같아질때까지 숫자를 하나씩 올려서 더해주기
#     for j in range(i, n+1):
#         sum += j
#         if sum == n: # 연속된 수 의 합이 n과 같다면 answer의 값을 올려줌
#             answer += 1
#             break
#         elif sum > n: # n을 넘기면 break를 통해 다음으로 넘어감
#             break
# # print(answer)


@elapsed
def solution(n):
    answer = 0
    for i in range(1, n+1): # 1부터 n까지
        sum = 0 # n과 같아질때까지 숫자를 하나씩 올려서 더해주기
        for j in range(i, n+1):
            sum += j
            if sum == n: # 연속된 수 의 합이 n과 같다면 answer의 값을 올려줌
                answer += 1
                break
            elif sum > n: # n을 넘기면 break를 통해 다음으로 넘어감
                break
    return answer
# 테스트 1 〉	통과 (6.04ms, 10.1MB)

print(solution(n))
