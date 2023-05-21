'''
https://school.programmers.co.kr/learn/courses/30/lessons/42862
체육복


문제 설명

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 
 학생에게만 체육복을 빌려줄 수 있습니다. 
 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 
 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.


제한사항

전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 
다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''
n = 20
lost = [
    28,
    22,
    20,
    2,
    26,
    10,
    16,
    4,
    14,
    8,
]
reserve = [
    27,
    1,
    15,
    7,
    25,
    19,
    9,
    13,
    3,
    21,
]
'''
1. 구해야 하는 것
    최대한 체육복을 많이 입히기
2. 1을 구하기 위해 필요한 것

3. 그 외 고려해야 할 사항
'''
# lost.sort()

# 학생들 = [1]*n

# for i in lost:
#     학생들[i-1] -= 1

# for i in reserve:
#     학생들[i-1] += 1

# for i in lost:
#     if i-1 in reserve:
#         학생들[i-1] += 1
#     if i+1 in reserve and i-1 not in reserve:
#         학생들[i-1] += 1
# print(학생들.sum())

#
# def solution(n, lost, reserve):
#     no_uni = set(lost) - set(reserve)
#     extra_uni = set(reserve) - set(lost)
#     for r in extra_uni:
#         no_uni.remove(r-1) if r-1 in no_uni else no_uni.remove(r+1) if r+1 in no_uni else None
#     return n - len(no_uni)

# def solution(n, lost, reserve):
#     no_uni = set(lost) - set(reserve)
#     for r in set(reserve) - set(lost):
#         no_uni.remove(r-1) if r-1 in no_uni else no_uni.remove(r+1) if r+1 in no_uni else None
#     return n - len(no_uni)


def solution(n, lost, reserve):
    no_uni = set(lost) - set(reserve)
    for r in set(reserve) - set(lost):
        no_uni = no_uni - {r-1} if {r-1} <= no_uni else no_uni - {r+1}
    return n - len(no_uni)


print(solution(n, lost, reserve))
