'''
https://school.programmers.co.kr/learn/courses/30/lessons/120883
로그인 성공?

문제 설명

머쓱이는 프로그래머스에 로그인하려고 합니다.
머쓱이가 입력한 아이디와 패스워드가 담긴 배열 id_pw와 
회원들의 정보가 담긴 2차원 배열 db가 주어질 때, 다음과 같이 
로그인 성공, 실패에 따른 메시지를 return하도록 solution 함수를 완성해주세요.

아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 
아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.


제한사항

회원들의 아이디는 문자열입니다.
회원들의 아이디는 알파벳 소문자와 숫자로만 이루어져 있습니다.
회원들의 패스워드는 숫자로 구성된 문자열입니다.
회원들의 비밀번호는 같을 수 있지만 아이디는 같을 수 없습니다.
id_pw의 길이는 2입니다.
id_pw와 db의 원소는 [아이디, 패스워드] 형태입니다.
1 ≤ 아이디의 길이 ≤ 15
1 ≤ 비밀번호의 길이 ≤ 6
1 ≤ db의 길이 ≤ 10
db의 원소의 길이는 2입니다.
'''

#
case1 = ["meosseugi", "1234"]	
case2 = ["programmer01", "15789"]	
case3 = ["rabbit04", "98761"]	
db1 = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
db2 = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]
db3 = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]

# def solution(id_pw, db):
#     # 리스트도 하나의 원소
#     # 일치하는 리스트가 있으면 바로 반환
#     if id_pw in db:
#         return "login"  

#     # db에 있는 각각의 원소(=id와 pw이 담긴 리스트)를 돌면서 
#     # id가 일치하는 항목이 있다면 "wrong pw" 리턴
#     # 없으면 continue로 계속하기
#     for row in db:
#         if row[0] in id_pw[0]:
#             return "wrong pw"
#         else:
#             continue
#     # 끝까지 못찾으면 "fail 반환"
#     return "fail"


# def solution(id_pw, db):
#     if id_pw in db:
#         return "login"  
#     for row in db:
#         if row[0] in id_pw[0]:
#             return "wrong pw"
#         else:
#             continue
#     return "fail"

def solution(id_pw, db):
    ids = []
    pws = []
    for i in db:
        ids.append(i[0])
        pws.append(i[1])
    if id_pw[0] not in ids:
        answer = "fail"
    elif id_pw[1] != pws[ids.index(id_pw[0])]:
        answer = "wrong pw"
    else:
        answer = "login"
    return answer


print(solution(case1, db1)) # "login"
print(solution(case2, db2)) # "wrong pw"
print(solution(case3, db3)) # "fail"
