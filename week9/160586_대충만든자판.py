'''

대충 만든 자판
문제 설명
휴대폰의 자판은 컴퓨터 키보드 자판과는 다르게 하나의 키에 여러 개의 문자가 할당될 수 있습니다. 
키 하나에 여러 문자가 할당된 경우, 동일한 키를 연속해서 빠르게 누르면 할당된 순서대로 문자가 바뀝니다.

예를 들어, 1번 키에 "A", "B", "C" 순서대로 문자가 할당되어 있다면 
1번 키를 한 번 누르면 "A", 두 번 누르면 "B", 세 번 누르면 "C"가 되는 식입니다.

같은 규칙을 적용해 아무렇게나 만든 휴대폰 자판이 있습니다. 
이 휴대폰 자판은 키의 개수가 1개부터 최대 100개까지 있을 수 있으며, 
특정 키를 눌렀을 때 입력되는 문자들도 무작위로 배열되어 있습니다. 
또, 같은 문자가 자판 전체에 여러 번 할당된 경우도 있고, 키 하나에 같은 문자가 여러 번 할당된 경우도 있습니다. 
심지어 아예 할당되지 않은 경우도 있습니다. 따라서 몇몇 문자열은 작성할 수 없을 수도 있습니다.

이 휴대폰 자판을 이용해 특정 문자열을 작성할 때, 
키를 최소 몇 번 눌러야 그 문자열을 작성할 수 있는지 알아보고자 합니다.

1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap과 
입력하려는 문자열들이 담긴 문자열 배열 targets가 주어질 때, 
각 문자열을 작성하기 위해 키를 최소 몇 번씩 눌러야 하는지 순서대로 
배열에 담아 return 하는 solution 함수를 완성해 주세요.

단, 목표 문자열을 작성할 수 없을 때는 -1을 저장합니다.


제한사항

1 ≤ keymap의 길이 ≤ 100
1 ≤ keymap의 원소의 길이 ≤ 100
keymap[i]는 i + 1번 키를 눌렀을 때 순서대로 바뀌는 문자를 의미합니다.
예를 들어 keymap[0] = "ABACD" 인 경우 1번 키를 한 번 누르면 A, 두 번 누르면 B, 세 번 누르면 A 가 됩니다.
keymap의 원소의 길이는 서로 다를 수 있습니다.
keymap의 원소는 알파벳 대문자로만 이루어져 있습니다.
1 ≤ targets의 길이 ≤ 100
1 ≤ targets의 원소의 길이 ≤ 100
targets의 원소는 알파벳 대문자로만 이루어져 있습니다.
'''


'''
1. 구해야 하는 것
    각 문자열을 작성하기 위해 키를 최소 몇번씩 눌러야 하는지
    작성할 수 없다면 -1
2. 1을 구하기 위해 필요한 것
    keymap의 원소별로 돌아가면서 target의 인덱스를 찾을 방법
    index번호끼리 비교해서 더 작은것을 채택?
    각각의 
3. 그 외 고려해야 할 사항
'''
keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
#[9, 4]
# keymap = ["AA"]
# targets = ["B"]
# #[-1]
# keymap = ["AGZ", "BSSS"]
# targets = ["ASA","BGZ"]
# #[4, 6]


최소누르는횟수 = {}
for k in keymap:
    print(k)
    for i, k in enumerate(k):
        print(i,k)
        if k not in 최소누르는횟수: # 인덱스 넘버기 때문에 +1을 해준다.
            최소누르는횟수[k] = i + 1
        else:
            최소누르는횟수[k] = min(최소누르는횟수[k], i + 1)
print(최소누르는횟수) #각각의 알파벳을 얻기 위해 가장 빠른 입력 횟수
답 = []
for target in targets:
    누른횟수 = 0
    for 글자 in target:
        print(글자)
        if 글자 not in 최소누르는횟수:
            누른횟수 = -1
            break
        else:
            누른횟수 += 최소누르는횟수[글자]
    답.append(누른횟수)
print(답)


# def solution(keymap, targets):
#     최소누르는횟수 = {}
#     for k in keymap:
#         for i, k in enumerate(k):
#             if k not in 최소누르는횟수:
#                 최소누르는횟수[k] = i + 1
#             else:
#                 최소누르는횟수[k] = min(최소누르는횟수[k], i + 1)
#     답 = []
#     for target in targets:
#         누른횟수 = 0
#         for 글자 in target:
#             if 글자 not in 최소누르는횟수:
#                 누른횟수 = -1
#                 break
#             else:
#                 누른횟수 += 최소누르는횟수[글자]
#         답.append(누른횟수)
#     return 답


# 최소누르는횟수[k] = {(i + 1) if k not in 최소누르는횟수 else min(최소누르는횟수[k], i + 1) for i, k in enumerate(k)}
def solution(keymap, targets):
    최소누르는횟수 = {}
    for k in keymap:
        for i, k in enumerate(k, 1):
            최소누르는횟수[k] = i if k not in 최소누르는횟수 else min(최소누르는횟수[k], i)            
    답 = []
    for target in targets:
        a = [-1 if 글자 not in 최소누르는횟수 else 최소누르는횟수[글자] for 글자 in target]
        답 += [-1] if -1 in a else [sum(a)]
    return 답

print(solution(keymap, targets))

# def solution(keymap, targets):
#     최소누르는횟수 = {}
#     for k in keymap:
#         for i, k in enumerate(k, 1):
#             최소누르는횟수[k] = i if k not in 최소누르는횟수 else min(최소누르는횟수[k], i)            
#     답 = [[-1] if -1 in [-1 if 글자 not in 최소누르는횟수 else 최소누르는횟수[글자] for 글자 in target] else [sum([-1 if 글자 not in 최소누르는횟수 else 최소누르는횟수[글자] for 글자 in target])] for target in targets]
#     return 답[0]+답[1]

# print(solution(keymap, targets))
