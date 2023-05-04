'''
https://school.programmers.co.kr/learn/courses/30/lessons/181921
배열 만들기 2


문제 설명

정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 
숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 
return 하는 solution 함수를 완성해 주세요.
만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.


제한사항

1 ≤ l ≤ r ≤ 1,000,000

'''
import math

l = 127
r = 1506

# 0과 5로만 이루어진 수 만들기?
# 5,
# 50, 55,
# 500, 505, 550, 555
# 5000, 5005, 5050, 5055, 5500, 5505, 5550, 5555


def solution(l, r):
    # 결과값을 담을 리스트
    result = []
    # for문에서 탐색 범위를 줄이기 위해 5의 배수로 만들어주기
    # 128이면 125이런식으로 바꿔준다 5로 나눈 몫에 5를 곱해서 가까운 5의 배수로 만들기
    num1 = l//5*5
    num2 = r//5*5 + 5
    # num1부터 num2 까지 5씩 체크하기
    for i in range(num1, num2, 5):
        print(set(str(i)))
        # 문자열도 set을 쓰면 집합으로 바꿔준다.
        # 0과 5 또는 5로만 이루어져 있다면 result에 추가해준다
        if set(str(i)) == set({"0", "5"}) or set(str(i)) == set({'5'}):
            result.append(i)
    return result if result else [-1]

    # 프로그래머스는 통과하지만 치명적인 오류가 하나 있다.
    # 숫자가 56이라고 하면 55를 기준으로 탐색을 해서 55을 포함시키게 된다.


print(solution(l, r))


def solution(l, r):
    result = []
    num1 = l//5*5
    num2 = r//5*5 + 5
    for i in range(num1, num2, 5):
        if set(str(i)) == set({"0", "5"}) or set(str(i)) == set({'5'}):
            result.append(i)
    return result if result else [-1]
