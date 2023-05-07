'''
https://school.programmers.co.kr/learn/courses/30/lessons/120924
다음에 올 숫자


문제 설명

등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 
마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.


제한사항

2 < common의 길이 < 1,000
-1,000 < common의 원소 < 2,000
common의 원소는 모두 정수입니다.
등차수열 혹은 등비수열이 아닌 경우는 없습니다.
등비수열인 경우 공비는 0이 아닌 정수입니다.
'''
common =[2, 4, 8]
# 16

# common = [1, 2, 3, 4]
# # 5

'''
1. 구해야 하는 것
    # 다음에 올 숫자
2. 1을 구하기 위해 필요한 것
    # 등차수열인지 등비수열인지 판단?
        # 어떻게 판별할지??
            # 다음 항과의 차가 일정한지를 계산
    # 공차 또는 공비를 더하거나 곱해준다.
3. 그 외 고려해야 할 사항
'''

# 등차수열인지 등비수열인지 판별?
a, b = common[2] - common[1], common[1] - common[0]

if a == b: # 같으면 등차수열
    print(common[-1] + a)
else:
    print(common[-1] * (common[1] / common[0]))



def solution(common):
    a, b = common[2] - common[1], common[1] - common[0]
    if a == b:
        return common[-1] + a
    else:
        return common[-1] * (common[1] / common[0])

# print(solution())


# if common[2] - common[1] == common[1] - common[0]:
#     print(common[-1] + common[2] - common[1])
# else:
#     print(common[-1] * (common[1] / common[0]))