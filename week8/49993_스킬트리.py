'''
https://school.programmers.co.kr/learn/courses/30/lessons/49993
스킬트리
문제 설명
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 썬더를 배우려면
먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 
따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만, 
썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 
매개변수로 주어질 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

제한 조건
스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
스킬 순서와 스킬트리는 문자열로 표기합니다.
예를 들어, C → B → D 라면 "CBD"로 표기합니다
선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
skill_trees는 길이 1 이상 20 이하인 배열입니다.
skill_trees의 원소는 스킬을 나타내는 문자열입니다.
skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.
'''


'''
1. 구해야 하는 것
    스킬트리 순서에 맞게 찍은 스킬트리의 개수
2. 1을 구하기 위해 필요한 것
    스킬트리가 skill의 원소들이 [:len(다른스킬을 뺀 스킬트리)] == skill
3. 그 외 고려해야 할 사항
'''
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# 2


count = 0
for s in skill_trees:
    for c in s:
        if skill.find(c) == -1:  # skill_trees에서 skill의 원소가 아닌 것들을 지워주기
            s = s.replace(c, '')
    if skill.find(s) == 0:  # skill에서 find로 찾은 index가 0이다 == 선행스킬부터 잘 찍었다.
        count += 1
print(count)


# answer = 0
# for sks in skill_trees:
#     sk_list = list(skill)
#     for sk in sks:
#         if sk in skill:
#             if sk != sk_list.pop(0):
#                 break
#     else:
#         answer += 1

# print(answer)


def solution(skill, skill_trees):
    count = 0
    for s in skill_trees:
        for c in s:
            if skill.find(c) == -1:
                s = s.replace(c, '')
        if skill.find(s) == 0:
            count += 1
    return count

# print(solution())
