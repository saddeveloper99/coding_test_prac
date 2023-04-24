'''
https://school.programmers.co.kr/learn/courses/30/lessons/120876
# 겹치는 선분의 길이

문제 설명

선분 3개가 평행하게 놓여 있습니다. 
세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 
형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
두 개 이상의 선분이 겹치는 부분의 길이를 
return 하도록 solution 함수를 완성해보세요.


제한사항

lines의 길이 = 3
lines의 원소의 길이 = 2
모든 선분은 길이가 1 이상입니다.
lines의 원소는 [a, b] 형태이며, a, b는 각각 선분의 양 끝점 입니다.
-100 ≤ a < b ≤ 100
'''
# my_string | result
case1 = [[0, 1], [2, 5], [3, 9]]	# 2
case2 = [[-1, 1], [1, 3], [3, 9]]	# 0
case3 = [[0, 5], [3, 9], [1, 10], [5, 9]]	# 8


from functools import reduce
def solution(lines):
    # a = []
    # cnt = 0
    # for line in lines:
    #     for dot in range(line[0], line[1]):
    #         if dot + 0.5 in a:
    #             cnt += 1
    #         else:
    #             a.append(dot + 0.5)
    # print(a)
    # return cnt

    # sorted_lines = sorted(lines)
    # a = sorted_lines[0][1] - sorted_lines[1][0] # 4
    # b = sorted_lines[1][1] - sorted_lines[2][0] # 7

    # print(a)
    # print(b)
    # if a > 0 and b > 0:
    #     return a + b
    # elif a > 0:
    #     return a
    # elif b > 0:
    #     return b
    # else:
    #     return 0    

    num_dict = {}
    for i in range(len(lines)): 
        for dot in range(lines[i][0], lines[i][1]+1):
            if i in num_dict.keys():
                num_dict[i].append(dot)
            else:
                num_dict[i] = [dot]
            
        # num_dict[0]
        # num_dict[1]
        # num_dict[2]

    print(num_dict)


# print(solution(case1))
# print(solution(case2))
print(solution(case3))