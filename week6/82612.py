'''
https://school.programmers.co.kr/learn/courses/30/lessons/82612
부족한 금액 계산하기

문제 설명

새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 
이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 
이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가
100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 
얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
단, 금액이 부족하지 않으면 0을 return 하세요.


제한사항

놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수

 
'''
price = 3
money = 20
count = 4
# 10

'''
1. 구해야 하는 것
    # 금액이 얼마나 모자란지 (아니면 0 반환)

2. 1을 구하기 위해 필요한 것
    # 놀이기구를 count번 탔을 때 비용의 합
        # for i in range(1, count+1)
        # cost에 i*price를 계속 더해주기
    # money에서 cost를 뺀다
'''

# 풀이
cost = 0
for i in range(1, count+1):
    cost += i*price
money - cost

print(cost)


# 제출용 함수
def solution(price, money, count):
    cost = 0
    for i in range(1, count+1):
        cost += i*price
    answer = -(money - cost) 
    return answer if answer > 0 else 0

print(solution(price, money, count))

