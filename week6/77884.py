'''
https://school.programmers.co.kr/learn/courses/30/lessons/77884
약수의 개수와 덧셈


문제 설명

두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 
약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 
하도록 solution 함수를 완성해주세요.


제한사항

1 ≤ left ≤ right ≤ 1,000
'''

l = 24
r = 27
# 52

'''
1. 구해야 하는 것
    # l부터 r까지 (약수의 개수가 짝수인 수의 합) - (약수의 개수가 홀수인 수의 합)
        # for i in range)
2. 1을 구하기 위해 필요한 것
    # 약수의 개수가 짝수인지 홀수인지 판별 
        # 해당 수의 약수의 개수
            # for문으로 a%b == 0인 약수 개수를 세기?
    # 약수의 개수를 저장한 자료형 
        # 1. 딕셔너리?
        # 2. cnt = 0?
    # if 약수의 개수 % 2 == 0: 짝수
    # else: 홀수
3. 그 외 고려사항
    # 약수의 개수는 기본적으로 1:j 2: j/2 이런식으로 페어가 있음.
    # 그런데 홀수라는 것은 제곱수라는 것.
    # if  i**(1/2) == int(i**(1/2))면 약수의 개수는 홀수
    # 위 식으로 판별 시 약수의 개수를 구할 필요가 없음.
'''


# 제출용 함수
def solution(l, r):
    answer = 0 
    for i in range(l,r+1):
        answer = answer - i if i**(1/2) == int(i**(1/2)) else answer + i
    return answer

# 풀이
answer = 0 
for i in range(l,r+1):
    if i**(1/2) == int(i**(1/2)): answer -= i 
    else: answer += i

print(answer)

# 제곱수인지 어떻게 판별?
    # for문으로 a*a == i가 나오는지?
    # 그냥 루트씌운 수가 정수인지
# print(25**(1/2) == int(25**(1/2)))