'''
https://school.programmers.co.kr/learn/courses/30/lessons/155652
둘만의 암호

문제 설명
두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 
다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.

문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
skip에 있는 알파벳은 제외하고 건너뜁니다.
예를 들어 s = "aukks", skip = "wbqd", index = 5일 때, 
a에서 5만큼 뒤에 있는 알파벳은 f지만 [b, c, d, e, f]에서 
'b'와 'd'는 skip에 포함되므로 세지 않습니다. 
따라서 'b', 'd'를 제외하고 'a'에서 5만큼 뒤에 있는 알파벳은 
[c, e, f, g, h] 순서에 의해 'h'가 됩니다. 나머지 "ukks" 또한 
위 규칙대로 바꾸면 "appy"가 되며 결과는 "happy"가 됩니다.

두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 
위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요.

제한사항
5 ≤ s의 길이 ≤ 50
1 ≤ skip의 길이 ≤ 10
s와 skip은 알파벳 소문자로만 이루어져 있습니다.
skip에 포함되는 알파벳은 s에 포함되지 않습니다.
1 ≤ index ≤ 20
 
'''

# ord() # 문자를 숫자로
# chr() # 숫자를 문자로

s = "aukks"
skip = "wbqd"
index = 5
# "happy"
# [b, c, d, e, f]
# [c, e, f, g, h]

########################### 제출용 함수 ############################

import string
def solution(s, skip, index):
    alpha = string.ascii_lowercase
    for i in skip:
        alpha = alpha.replace(i, "")

    result = ''
    if index > len(alpha):
        index = index % len(alpha)
    for j in s:
        a = alpha.index(j)
        try:
            result += alpha[a + index]
        except:
            result += alpha[a + index - len(alpha)]
    return result

print(solution(s, skip, index))


#################### 유니코드 > 스킵 > 풀이 #######################
# alpha = [ord(i) for i in s]
#   # 처음 문자열(s)를 아스키 코드로 변환한 문자열들의 리스트
 
# index_board = [i for i in range(97, 123)]
#   # 문자열의 아스키 코드 범위
 
# skip_list = [ord(i) for i in skip]
  # 스킵할 문자열(skip)을 아스키 코드로 변환한 문자열들의 리스트

 
#  index_board 에서 skip_list 의 원소들을 삭제 후
 
#  alpha 의 각각의 원소들을 index_board 에서 찾아서 원래 인덱스 + index만큼 해준 뒤 새로운 리스트에 추가
 
#  이때 만약 index_board 의 범위를 넘어갈 경우 IndexError가 발생할 것이므로
 
#  try - except를 사용해서 해당 경우에 index_board 의 길이만큼을 추가로 빼주었는데, 
 
#  그럼에도 불구하고 index의 크기가 너무 커서 z 에서 a로 두번이상 갈 경우 역시 IndexError가 발생.
 
#  조건문을 사용해서 index가 index_board 의 길이보다 클 경우, index를 index % len(index_board)로 값을 변경해주었다.

alpha = [ord(i) for i in s]
index_board = [i for i in range(97, 123)]
skip_list = [ord(i) for i in skip]

for i in skip_list:
    if i in index_board:
        index_board.remove(i)

answer = []
result = ""

for i in alpha:
    if index > len(index_board):
        index = index % len(index_board)
    a = index_board.index(i) 
    try: 
        answer.append(index_board[a + index])
    except:
        answer.append(index_board[a + index - len(index_board)])
for i in answer:
    result += chr(i) 



####################### 처음 풀이(실패) ##############################
#     str_num = index_board.index(i)
#     if index_board[str_num + index] >= 123:
#         answer.append(index_board[str_num + index] - 26)
#     else:
#         answer.append(index_board[str_num + index])

# for i in answer:
#     result += chr(i)

# print(result)

# print("원래 문자열(유니코드) : ",alpha)
# print("스킵할 문자열(유니코드) : ",skip_list)
# print("스킵용 보드 : ", index_board, len(index_board))
# # print(answer)

# def solution(s, skip, index):
#     alpha = [ord(i) for i in s]
#     skiplist = [ord(i) for i in skip]

#     index_board = [i for i in range(min(alpha), max(alpha)+len(skip)+index)]
#     for i in skiplist:
#         if i in index_board:
#             index_board.remove(i)

#     answer = []
#     result = ''
#     for i in alpha:
#         str_num = index_board.index(i)
#         if index_board[str_num + index] >= 123:
#             answer.append(index_board[str_num + index] - 26)
#         else:
#             answer.append(index_board[str_num + index])

#     for i in answer:
#         result += chr(i)
#     return result

