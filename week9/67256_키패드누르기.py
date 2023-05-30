'''
https://school.programmers.co.kr/learn/courses/30/lessons/67256
[카카오 인턴] 키패드 누르기

문제 설명

스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.

이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 
입력하려고 합니다. 맨 처음 왼손 엄지손가락은 * 키패드에 
오른손 엄지손가락은 # 키패드 위치에서 시작하며, 
엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 
키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 
현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 
왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 
왼손잡이인지 오른손잡이인지를 나타내는 문자열 hand가 매개변수로 주어질 때,
 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 
 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.


제한사항

numbers 배열의 크기는 1 이상 1,000 이하입니다.
numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
hand는 "left" 또는 "right" 입니다.
"left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
왼손 엄지손가락을 사용한 경우는 L, 
오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 
문자열 형태로 return 해주세요.
'''

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
# hand = "left"

# "LRLLLRLLRRL"
'''
1. 구해야 하는 것

2. 1을 구하기 위해 필요한 것

3. 그 외 고려해야 할 사항
'''
# if (i // 3) == l_hand[0] and  (i // 3) != r_hand[0]:
#     l_hand[0] = i // 3
#     result.append("L")
#     print("왼손",i, l_hand)
# elif (i // 3) == r_hand[0] and (i // 3) != l_hand[0]:
#     r_hand[0] = i // 3 - 1 
#     result.append("R")
#     print("오른손",i, r_hand)
# else:
#     print(i, l_hand,r_hand)

# result = []
# l_hand = [3,0]
# r_hand = [3,2]
# for i in numbers:
#     x, y = (i // 3), (i % 3 - 1)
#     if i in [1,4,7]:
#         l_hand[0] = i // 3
#         l_hand[1] = i % 3 - 1
#         result.append("L")
#         print("왼손", i, l_hand)
#     elif i in [3,6,9]:
#         r_hand[0] = i // 3 - 1 
#         r_hand[1] = i % 3 
#         result.append("R")
#         print("오손", i, r_hand)
#     else:
#         if i == 0:
#             i = 11
#         l = abs((i // 3) - l_hand[0]) + abs(1 - l_hand[1])
#         r = abs((i // 3) - r_hand[0]) + abs(1 - r_hand[1])
#         print(l_hand, r_hand)
#         print(i, l, r)
#         if l > r:
#             r_hand[0] = i // 3
#             r_hand[1] = i % 3 - 1
#             result.append("R")
#             print("오손",i, r_hand)
#         elif l < r:
#             l_hand[0] = i // 3
#             l_hand[1] = i % 3 - 1
#             result.append("L")
#             print("왼손",i, l_hand)
#         elif l==r:
#             if hand == "right":
#                 r_hand[0] = i // 3
#                 r_hand[1] = i % 3 - 1
#                 result.append("R")
#                 print("오손",i, r_hand)
#             else:
#                 l_hand[0] = i // 3
#                 l_hand[1] = i % 3 - 1
#                 result.append("L")
#                 print("왼손",i, l_hand)
# print(result)


# from sys import path
# path.append("../codingtest_prac")
# import timechecker
# timecheckers.timechecker.py



# @timechecker.elapsed

def solution(numbers, hand):
    left, middle, right = [1, 4, 7], [2, 5, 8, 0], [3, 6, 9]
    l_hand, r_hand = [3,0], [3,2]
    result = []
    for i in numbers:
        def presskey(pos, which_hand):
            x, y = (i // 3, i % 3 - 1) if pos != right else (i // 3 - 1, i % 3)
            if which_hand == "l":
                l_hand[0],l_hand[1] = x, y
                result.append("L")
            else:
                r_hand[0], r_hand[1] = x, y
                result.append("R")
        if i in left:
            presskey(left, "l")
        elif i in right:
            presskey(right, "r")
        else:
            if i == 0: i = 11
            ld = abs((i // 3) - l_hand[0]) + abs(1 - l_hand[1])
            rd = abs((i // 3) - r_hand[0]) + abs(1 - r_hand[1])
            if ld > rd:
                presskey(middle, "r")
            elif ld < rd:
                presskey(middle, "l")
            elif ld == rd:
                if hand == "right":
                    presskey(middle, "r")
                else:
                    presskey(middle, "l")
    return ''.join(result)

print(solution(numbers, hand))

