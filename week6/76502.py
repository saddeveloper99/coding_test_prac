'''
https://school.programmers.co.kr/learn/courses/30/lessons/76502
괄호 회전하기

문제 설명
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 
예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 
예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, 
{}([]) 도 올바른 괄호 문자열입니다.
대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 
s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 
solution 함수를 완성해주세요.
 
'''

'''
1. 구해야 하는 것
    # 괄호로만 이루어진 문자열 s를 왼쪽으로 회전시켜서 
    # 올바른 괄호문자열이 되는 x의 개수
2. 1을 구하기 위해 필요한 것
    # 이동시킨 문자열이 유효한가를 판단 및 삭제
        # 스택에 하나씩 쌓아가면서, 스택에 만약 여는 괄호가 있고,
        # 마지막으로 들어온 원소가 닫는 괄호라면 둘다 없애기
    # 회전시킬 방법
        # for문을 사용해 원소를 슬라이싱해서 불이기
3. 그 외 고려해야 할 사항
    # 스택?
    # 시간복잡도?
'''
# case 1
# ](){}[ x
# (){}[] o
# ){}[]( x
# {}[]() o 
# }[](){ x
# [](){} o

# case 2
# ]()[{} x
# ()[{}] o
# )[{}]( x
# [{}]() o
# {}]()[ x
# }]()[{ x

s = "}]()[{" # 3

# answer = 0
# for i in range(len(s)):
#     s_spin = s[i+1:]+s[:i+1]
#     stack = ''
#     # print(s_spin)
#     for i in s_spin:
#         stack += i
#         if stack:
#             if '(' in stack and stack[-1] == ')':
#                 stack = stack.replace(')',"")
#                 stack = stack.replace('(',"")
#             if '{' in stack and stack[-1] == '}':
#                 stack = stack.replace('}',"")
#                 stack = stack.replace('{',"")
#             if '[' in stack and stack[-1] == ']':
#                 stack = stack.replace(']',"")
#                 stack = stack.replace('[',"")
#     if not stack:
#         answer += 1



s.replace()

def solution(s):
    answer = 0
    for i in range(len(s)):
        s_spin = s[i+1:]+s[:i+1]
        stack = ''
        # print(s_spin)
        for i in s_spin:
            stack += i
            if stack:
                if '(' in stack and stack[-1] == ')':
                    stack = stack.replace(')',"")
                    stack = stack.replace('(',"",1)
                if '{' in stack and stack[-1] == '}':
                    stack = stack.replace('}',"")
                    stack = stack.replace('{',"",1)
                if '[' in stack and stack[-1] == ']':
                    stack = stack.replace(']',"")
                    stack = stack.replace('[',"",1)
        if not stack:
            answer += 1
    return answer

# def solution(s):
#     answer = 0
#     for i in range(len(s)):
#         s_spin = s[i+1:]+s[:i+1]
#         stack = ''
#         for i in s_spin:
#             stack += i
#             if '()' in stack:
#                 stack = stack.replace('()','')  
#             if '[]' in stack:
#                 stack = stack.replace('[]','')
#             if '{}' in stack:
#                 stack = stack.replace('{}','')
#         if not stack:
#             answer += 1
#     return answer

print(solution(s))

# 다른 분 풀이 
def solution(s):
    answer = 0
    for _ in s:
        s=s[1:]+s[:1] 
        a=s 
        while "()" in a or "[]" in a or "{}" in a: 
            a=a.replace("()","").replace("[]","").replace("{}","")
            if a == "":
                answer += 1
    return answer