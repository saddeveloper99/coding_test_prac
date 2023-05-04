'''
https://school.programmers.co.kr/learn/courses/30/lessons/181943
문자열 겹쳐쓰기

문제 설명
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 
문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 
문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를
작성해 주세요.

제한사항
my_string와 overwrite_string은 숫자와 알파벳으로 이루어져 있습니다.
1 ≤ overwrite_string의 길이 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ my_string의 길이 - overwrite_string의 길이

'''

my_string = "He11oWor1d"
overwrite_string = "lloWorl"
s = 2
# result = "HelloWorld"

# 11oWor1 > lloWorl
# [my_string의 인덱스 s:overwrite_string의 길이]

# my_string의 인덱스 s
# overwrite_string의 길이
# 슬라이싱해서 접합수술

#  c = my_string[s:s+b]
def solution(my_string, overwrite_string, s):
    a = len(overwrite_string) # 7
    b = my_string[:s] + overwrite_string + my_string[s+a:]
    return b


# a.split()

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
