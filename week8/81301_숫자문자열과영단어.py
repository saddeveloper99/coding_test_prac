'''
https://school.programmers.co.kr/learn/courses/30/lessons/81301
숫자 문자열과 영단어

문제 설명
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 
일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 
그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 
return 하도록 solution 함수를 완성해주세요.

참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine
'''
s = "one4seveneight"
# 1478

'''
1. 구해야 하는 것
    # s에서 영단어에 해당하는 것들을 숫자로 바꾼 문자열
2. 1을 구하기 위해 필요한 것
    # 어떻게 찾을것인지
        # find?
        # 그냥 replace
    # 어떻게 바꿀것인지
        # replace?
3. 그 외 고려해야 할 사항
'''
number_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

a = s
for i, j in number_dict.items():
    # print(i, j)
    # a = s.replace(i, j)
    a = a.replace(i, j)
print(s)
print(a)


def solution(s):
    number_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    a = s
    for i, j in number_dict.items():
        a = a.replace(i, j)
    return int(a)