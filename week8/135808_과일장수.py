'''
https://school.programmers.co.kr/learn/courses/30/lessons/135808
과일 장수

문제 설명
과일 장수가 사과 상자를 포장하고 있습니다. 사과는 상태에 따라 
1점부터 k점까지의 점수로 분류하며, k점이 최상품의 사과이고 1점이 최하품의 사과입니다. 
사과 한 상자의 가격은 다음과 같이 결정됩니다.

한 상자에 사과를 m개씩 담아 포장합니다.
상자에 담긴 사과 중 가장 낮은 점수가 p (1 ≤ p ≤ k)점인 경우, 
사과 한 상자의 가격은 p * m 입니다.
과일 장수가 가능한 많은 사과를 팔았을 때, 얻을 수 있는 최대 이익을 계산하고자 합니다.
(사과는 상자 단위로만 판매하며, 남는 사과는 버립니다)

예를 들어, k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면, 
다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 
얻을 수 있습니다.

(최저 사과 점수) x (한 상자에 담긴 사과 개수) x (상자의 개수) = 2 x 4 x 1 = 8
사과의 최대 점수 k, 한 상자에 들어가는 사과의 수 m, 사과들의 점수 score가 
주어졌을 때, 과일 장수가 얻을 수 있는 최대 이익을 
return하는 solution 함수를 완성해주세요.

제한사항
3 ≤ k ≤ 9
3 ≤ m ≤ 10
7 ≤ score의 길이 ≤ 1,000,000
1 ≤ score[i] ≤ k
이익이 발생하지 않는 경우에는 0을 return 해주세요.

'''

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

'''
1. 구해야 하는 것
    각각의 상자 가격들의 합이 최대일때의 이익
2. 1을 구하기 위해 필요한 것
    최대가 되려면? 최저가의 사과들끼리, 품질 좋은 사과끼리 분리해야함
        sort로 정렬 후 m개 씩 끊어서 담기
            개수가 모자라면 세지 않음
3. 그 외 고려해야 할 사항
'''

result = 0
score.sort(reverse=True)  # 내림차순 정렬
# print(score)
for i in range(0, len(score), m):  # 0부터 / 사과 개수-1까지 / m개씩 건너뛰면서
    a = score[i:i+m]  # 이거 왜 에러 안남
    print(a)
    # 사과가 모두 담긴 박스만
    if len(a) == m:
        # (최저 사과 점수) x (한 상자에 담긴 사과 개수)
        result += min(a)*m
print(result)

# print("????? :", score[:99999999999999])
# 아마 입력한 999999999..가 min(입력값, len())으로 알아서 더 작은걸로 걸러주지 않을까?


# def solution(k, m, score):
#     result = 0
#     score.sort(reverse=True)
#     for i in range(0, len(score), m):
#         a = score[i:i+m]
#         if len(a) == m:
#             result += min(a)*m
#     return result
# # print(solution(k, m, score))


def solution(k, m, score):
    return sum(sorted(score)[len(score) % m::m])*m


def solution(k, m, score):
    a = len(score) % m  # (사과 개수)를 (한 상자당 사과 개수)로 나눈 나머지 = 버려야 할 부분!!
    b = sorted(score)  # 사과를 품질별 오름차순 정렬
    c = b[a::m]  # 사과를 품질별 오름차순 정렬한 리스트를 필요없는 부분 제끼고 m개씩 나누기
    # 오름차순 정렬이므로 m개씩 나누면 첫번째 원소가 최솟값이 된다.
    d = sum(c)  # sum으로 상자별 최소 사과가격을 모두 더함
    print(a)
    print(b)
    print(c)
    print(d)
    return d*m  # 상자개수를 곱해서 총 수익 구하기


print(solution(k, m, score))
