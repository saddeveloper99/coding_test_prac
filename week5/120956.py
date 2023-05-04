'''
https://school.programmers.co.kr/learn/courses/30/lessons/120956
옹알이 (1)

문제 설명
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다.
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을
최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다.
문자열 배열 babbling이 매개변수로 주어질 때,
머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록
solution 함수를 완성해주세요.

제한사항
1 ≤ babbling의 길이 ≤ 100
1 ≤ babbling[i]의 길이 ≤ 15
babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는
각각 최대 한 번씩만 등장합니다.
즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가
한 번씩만 등장합니다.
문자열은 알파벳 소문자로만 이루어져 있습니다.

'''

# babbling = ["aya", "yee", "u", "maa", "wyeoo"]
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]


ong_al = ["aya", "ye", "woo", "ma"]
cnt = 0
for i in babbling:
    for j in ong_al:
        if j in i:
            i = i.replace(j, "1", 1)
    if i.isdigit():
        cnt += 1


print(cnt)

# 현재 문제점들
# maya는 ma랑 aya가 둘다 있는데 어떡함?
# wyeoo는 ye를 지우면 woo가 새로 생겨서 문제


def solution():
    ong_al = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        for j in ong_al:
            if j in i:
                i = i.replace(j, "1", 1)
        if i.isdigit():
            cnt += 1
    return cnt
