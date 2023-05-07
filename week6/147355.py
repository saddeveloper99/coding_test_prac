'''
https://school.programmers.co.kr/learn/courses/30/lessons/147355
크기가 작은 부분문자열


문제 설명

숫자로 이루어진 문자열 t와 p가 주어질 때, t에서 p와 길이가 같은 부분문자열 
중에서, 이 부분문자열이 나타내는 수가 p가 나타내는 수보다 작거나 같은 것이 
나오는 횟수를 return하는 함수 solution을 완성하세요.

예를 들어, t="3141592"이고 p="271" 인 경우, t의 길이가 3인 부분 문자열은 
314, 141, 415, 159, 592입니다. 이 문자열이 나타내는 수 중 271보다 작거나 
같은 수는 141, 159 2개 입니다.


제한사항

1 ≤ p의 길이 ≤ 18
p의 길이 ≤ t의 길이 ≤ 10,000
t와 p는 숫자로만 이루어진 문자열이며, 0으로 시작하지 않습니다.
'''
t = "500220839878"
p = "7"
'''
1. 구해야 하는 것
    # t의 부분 문자열 중 p보다 작거나 같은 것이 나오는 횟수
2. 1을 구하기 위해 필요한 것
    # t의 부분 문자열을 나눌 방법
        # for문으로 슬라이싱
        # 슬라이싱한 문자열들을 리스트에?
    # 비교하는 방법
        # 슬라이싱한 원소들을 하나씩 비교?
        # p를 부분 문자열 리스트에 넣고 sort해서 인덱스를 반환?
3. 그 외 고려해야 할 사항
    # t와 p는 0으로 시작하지 않는 숫자로만 이루어진 문자열
'''
result = 0
for i in range(len(t)-len(p)+1):  # 부분 문자열, 
    part = t[i:i+len(p)]  # i부터 len(p)개 잘라냄
    # print(part)
    if int(part) <= int(p):  # str이므로 둘다 int씌워서 비교 # 안해도 된다!!
        result += 1 
print(result)


def solution(t, p):
    result = 0
    for i in range(len(t)-len(p)+1):
        part = t[i:i+len(p)]
        if int(part) <= int(p):
            result += 1
    return result
# print(solution())


def solution(t, p):
    return len([1 for i in range(len(t)-len(p)+1) if int(t[i:i+len(p)]) <= int(p)])
