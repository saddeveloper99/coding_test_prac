# https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 문자열 정렬하기 (1)

# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때, 
# my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 
# solution 함수를 작성해보세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# my_string에는 숫자가 한 개 이상 포함되어 있습니다.
# my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다.

# my_string | result
case1 = "hi12392"	# [1, 2, 2, 3, 9]
case2 = "p2o4i8gj2"	# [2, 2, 4, 8]
case3 = "abcde0"	# [0]

def solution(a):
    
    # # 리스트를 하나 만들어서 a문자열을 돌면서 문자열이 숫자인지 확인
    # # 숫자라면 리스트에 int값으로 추가해주기
    # result = []
    # for i in a:
    #     if i.isdigit():
    #         result.append(int(i))
    # # 정렬
    # return sorted(result)
    

    # a문자열을 돌면서 int(i)를 해주는데, 만약 문자열이면 ValueError 발생
    # try except로 예외처리
    result = []
    for i in a:
        try:
            result.append(int(i))
        # 에러 발생 시 다음 원소부터 다시 리스트에 넣기
        except ValueError: 
            continue
        # 정렬
    return sorted(result)
    
print(solution(case1))
print(solution(case2))
print(solution(case3))

def solution(a):
    result = []
    for i in a:
        try:
            result.append(int(i))
        except ValueError: 
            continue
    return sorted(result)