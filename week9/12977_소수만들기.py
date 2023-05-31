'''
https://school.programmers.co.kr/learn/courses/30/lessons/12977
소수 만들기

문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 
서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 
solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
'''
from sys import path
path.append("../codingtest_prac")
from timecheckers.timechecker import elapsed
'''
1. 구해야 하는 것
    3개를 더해서 소수가 되는 개수
2. 1을 구하기 위해 필요한 것
    소수 판별 > 에라토스테네스의 체?
    그냥 제곱근까지 구하기?
3. 그 외 고려해야 할 사항
'''
nums = [i for i in range(200)]

# def isprime(n):
#     numbers = set(range(2,n+1))
#     for i in range(2, int(n**0.5) + 1):
#         if i in numbers:
#             numbers -= set(range(i*2, n+1, i))
#     return True if len(numbers) == 1 else False
# ? 이거 구하는거 아니네



from itertools import combinations as c
##############################################################
# * 그냥 풀이 
def isprime1(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    # count = sum([1 for i in range(2, int(n**0.5) + 1) if n % i == 0])
    return True
@elapsed
def solution1(nums):
    answer = []
    for i in c(nums, 3):
        answer.append(isprime1(sum(i)))
    return answer.count(True)
    # return sum([isprime(sum(i)) for i in c(nums, 3)])


############################################################## 
# * 숏코딩1 
def isprime2(n):
    count = sum([1 for i in range(2, int(n**0.5) + 1) if n % i == 0])
    return True if not count else False

@elapsed
def solution2(nums):
    return sum([isprime2(sum(i)) for i in c(nums, 3)])

##############################################################
# * 에라토스테네스의 체?
def isprime3(n):
    numbers = set(range(2,n+1))
    for i in range(2, int(n**0.5) + 1):
        if i in numbers:
            numbers -= set(range(i*2, n+1, i))
    return True if {n} <= numbers else False

@elapsed
def solution3(nums):
    return sum([isprime3(sum(i)) for i in c(nums, 3)])


##############################################################
# * 숏코딩?
def isprime(n):
    return True if not sum([1 for i in range(2, int(n**0.5) + 1) if n % i == 0]) else False
@elapsed
def solution(nums):
    return sum([isprime(sum(i)) for i in c(nums, 3)])


print("그냥 풀이 : ",solution1(nums)) # solution1 elapsed: 0.076227sec (real) / 0.046875sec (cpu)
print("숏코딩1 : ",solution2(nums)) # solution2 elapsed: 0.139236sec (real) / 0.093750sec (cpu)
print("에라토스 : ",solution3(nums)) # solution3 elapsed: 1.163033sec (real) / 0.656250sec (cpu)
print("숏코딩2 : ", solution(nums)) # solution elapsed: 0.137546sec (real) / 0.109375sec (cpu)

