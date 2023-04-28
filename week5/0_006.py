'''
https://school.programmers.co.kr/learn/courses/30/lessons/131128
숫자 짝꿍

문제 설명
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 
만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 
서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다.
X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 
공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 
공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다
(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

제한사항
3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
X, Y는 0으로 시작하지 않습니다.
X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.
'''
from collections import Counter

X = "10523405"
Y = "23455"

# X = "100"
# Y = "203045"

# X = "12321"
# Y = "42531"

def solution(X, Y):
    # Counter는 해당 문자열에 문자가 각각 몇개인지 .ex) a는 4개, b는 6개 이런식으로 세주는 친구
    # 지금 여기서는 0은 몇개 1은 몇개 2는 몇개 이런식으로 세줄 것.
    # 그렇게 X의 {0은 몇개 1은 몇개 2는 몇개}와 Y의 {0은 몇개 ..}의 원소의 교집합!?
    # &는 불변형 자료형은 모두 사용할 수 있다.

    intersection = list((Counter(X) & Counter(Y)).elements())
    intersection.sort(reverse=True)

    print("X의 문자열 별 개수 : ", Counter(X))       
    # Counter({'0': 2, '5': 2, '1': 1, '2': 1, '3': 1, '4': 1})   
    print("X와 Y의 교집합 : ", Counter(X) & Counter(Y))
    # Counter({'5': 2, '2': 1, '3': 1, '4': 1})
    print("X와 Y의 교집합.elements : ", (Counter(X) & Counter(Y)).elements())
    # <itertools.chain object at 0x000002C7C9CAB9A0>
    print("X와 Y의 교집합 리스트 : ", intersection)
    # ['5', '5', '4', '3', '2']

    a = "".join(sorted(intersection, reverse=True))
    if set(a) == {"0"}:
        return "0"
    elif a == "":
        return "-1"
    else:
        return a
    

# def solution(X, Y):
#     intersection = []
#     a, b = list(X), list(Y)

#     # a의 모든 원소를 순회
#     for i in a:
#         # a의 모든 원소가 b의 모든 원소를 순회하면서 일치하는지 비교
#         # 여기서 이미 원소 개수가 많아지면 out..
#         if i in b:
#             intersection.append(i)
#             b.pop(b.index(i))
        
#     a = "".join(sorted(intersection, reverse=True))
#     print(a)
#     if set(a) == {"0"}:
#         return "0"
#     elif a == "":
#         return "-1"
#     else:
#         return a



print(solution(X, Y))


from collections import Counter
def solution(X, Y):
    intersection = list((Counter(X) & Counter(Y)).elements())
    intersection.sort(reverse=True)

    a = "".join(sorted(intersection, reverse=True))
    if set(a) == {"0"}:
        return "0"
    elif a == "":
        return "-1"
    else:
        return a