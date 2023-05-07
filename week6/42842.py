'''
https://school.programmers.co.kr/learn/courses/30/lessons/42842
카펫

문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 
테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 
기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 
주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 
solution 함수를 작성해주세요.


제한사항

갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
 
'''
brown = 10
yellow = 2
# [4, 3]
'''
1. 구해야 하는 것
    # 카펫의 가로, 세로
2. 1을 구하기 위해 필요한 것
    # 가로 세로를 어떻게 구할지??
    # 넓이 = yellow + brown
    # brown의 면적 = 2*세로 + 2*가로 - 4
    # yellow의 면적 = (가로-2) * (세로-2)
3. 그 외 고려해야 할 사항
    # 카펫의 긴쪽이 가로
    # yellow는 1 이상(가로, 세로 최소 길이는 3부터 시작한다)
'''

s = yellow + brown  # 넓이
for height in range(3, s//3+1):  # 세로 길이 후보 i
    if s % height == 0:  # 넓이를 세로 길이로 나눌 수 있다면
        width = s / height  # 그것은 가로길이 후보
        if (height - 2) * (width - 2) == yellow: # yellow의 면적 = (가로-2) * (세로-2)
            print([width, height])


def solution(brown, yellow):
    s = yellow + brown
    for height in range(3, s//3+1):
        if s % height == 0:
            width = s / height
            if (height - 2) * (width - 2) == yellow:
                return [width, height]



# print(solution())
