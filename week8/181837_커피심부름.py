'''
https://school.programmers.co.kr/learn/courses/30/lessons/181837
커피 심부름

문제 설명

팀의 막내인 철수는 아메리카노와 카페 라테만 판매하는 카페에서 팀원들의 커피를 
사려고 합니다. 아메리카노와 카페 라테의 가격은 차가운 것과 뜨거운 것 상관없이 
각각 4500, 5000원입니다. 각 팀원에게 마실 메뉴를 적어달라고 하였고, 
그 중에서 메뉴만 적은 팀원의 것은 차가운 것으로 통일하고 "아무거나"를 적은 팀원의 것은 
차가운 아메리카노로 통일하기로 하였습니다.

각 직원이 적은 메뉴가 문자열 배열 order로 주어질 때, 
카페에서 결제하게 될 금액을 return 하는 solution 함수를 작성해주세요. 
order의 원소는 아래의 것들만 들어오고, 각각의 의미는 다음과 같습니다.

order의 원소	의미
"iceamericano", "americanoice"	차가운 아메리카노
"hotamericano", "americanohot"	따뜻한 아메리카노
"icecafelatte", "cafelatteice"	차가운 카페 라테
"hotcafelatte", "cafelattehot"	따뜻한 카페 라테
"americano"	아메리카노
"cafelatte"	카페 라테
"anything"	아무거나
'''
from timecheckers.timechecker import elapsed


'''
1. 구해야 하는 것
    총 음료들의 가격의 합
2. 1을 구하기 위해 필요한 것
    아이스나 핫이나 가격은 똑같으니 아메리카노냐 카페라떼냐를 판별
    아무거나 == 아아 이므로 아무거나도 4500원

3. 그 외 고려해야 할 사항
'''
order = ["cafelatte", "americanoice", "hotcafelatte", "anything"]
# order = ["cafelatte"]* 10000000

# 19000

total = 0
for i in order:
    if "cafelatte" in i:
        total += 5000
    elif "americano" in i or "anything" == i:
        total += 4500
print(total)



import re
total = 0
for i in order:
    if re.search(r"cafelatte", i):
        total += 5000
    elif re.search(r"americano|anything", i):
        total += 4500
print(total)


total = sum(map(lambda i: 5000 if "cafelatte" in i else 4500, order))
total = sum(5000 if "cafelatte" in i else 4500 for i in order)


print(total)

import time


start = time.time()
# @elapsed
def solution(order):
    total = 0
    for i in order:
        if "cafelatte" in i:
            total += 5000
        elif "americano" in i or "anything" == i:
            total += 4500   
    return total
print(solution(order))
print("time3 :", time.time() - start)