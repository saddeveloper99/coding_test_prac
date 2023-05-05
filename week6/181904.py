'''
https://school.programmers.co.kr/learn/courses/30/lessons/181904
세로 읽기

문제 설명
문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 
m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 
문자열로 return 하는 solution 함수를 작성해 주세요.

제한사항
my_string은 영소문자로 이루어져 있습니다.
1 ≤ m ≤ my_string의 길이 ≤ 1,000
m은 my_string 길이의 약수로만 주어집니다.
1 ≤ c ≤ m

'''
my_string = "ihrhbakrfpndopljhygc"  # happy
m = 4
c = 2
'''
1. 구해야 하는 것
    # m글자씩 가로로 적었을 때, 세로로 c열에 적힌 글자들의 문자열

2. 1을 구하기 위해 필요한 것
    # m씩 자르는 방법

    # c씩 출력하는 방법

    # 슬라이싱

3. 그 외 고려해야 할 사항
'''

# 풀이
print(my_string[c-1::m])



# 제출용 함수
def solution(my_string, m, c):
    return my_string[c-1::m]


# 한줄
solution = lambda my_string, m, c: my_string[c-1::m]



