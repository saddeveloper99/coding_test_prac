'''
https://school.programmers.co.kr/learn/courses/30/lessons/68935
3진법 뒤집기


문제 설명

자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 
이를 다시 10진법으로 표현한 수를 
return 하도록 solution 함수를 완성해주세요.


제한사항

n은 1 이상 100,000,000 이하인 자연수입니다.

'''

# 3^4 ,3^3 ,3^2, 3
# 81   27   9    3


n = 64


# def solution(n):
#     a = n
#     b = []
#     answer = 0

#     while a >= 1:
#         b.append(a % 3)
#         a = a//3
#     print("뒤집힌 3진법은",b)
    
#     # len(b)까지
#     # answer에 
#     for i in range(len(b)):
#         answer += b[i] * (3 ** (len(b) - i - 1))
#     return answer
    




# print(int('2000', 3))

def solution(n):
    a = n
    b = []
    while a >= 1:
        b.append(a % 3)
        a = a // 3
    answer = 0
    for i in range(len(b)):
        answer += b[i] * (3 ** (len(b) - i - 1))
    return answer
        
print(solution(n))