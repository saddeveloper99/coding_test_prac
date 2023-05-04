'''
https://school.programmers.co.kr/learn/courses/30/lessons/12915
문자열 내 마음대로 정렬하기


문제 설명
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 
각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.


제한사항
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 
사전순으로 앞선 문자열이 앞쪽에 위치합니다.
'''

# strings = ["sun", "bed", "car"]
# n = 1
strings = ["efage", "begaqed", "cqqeear"]
n = 4

# 풀이
# sort의 key인자에 어떻게 잘 하면...?

def solution(strings, n):
    # 같은 문자열이 여럿일 경우를 생각해서 그냥 sort를 한번 한뒤 
    # key를 strings안의 문자열 x에 대해 x[n]번째 인덱스를 key로 sort
    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings

print(solution(strings, n))

# 제출용
def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings