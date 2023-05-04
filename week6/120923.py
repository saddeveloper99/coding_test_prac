'''
https://school.programmers.co.kr/learn/courses/30/lessons/120923
연속된 수의 합

문제 설명
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때,
정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

제한사항
1 ≤ num ≤ 100
0 ≤ total ≤ 1000
num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.


 
'''
num = 4
total = 14
# 2 3 4 5

# 홀수/짝수
# 3 4 5 = 12

# total//num?
middle_num = total//num

if num % 2 == 1:
    answer = [i for i in range(middle_num - num//2, middle_num + num//2 + 1)]
else:
    answer = [i for i in range(middle_num - num//2+1, middle_num + num//2 + 1)]

print(answer)


# for i in range(middle_num - num//2,middle_num + num//2 + 1):
#     print(i)


def solution(num, total):
    middle_num = total//num
    if num % 2 == 1:
        answer = [i for i in range(middle_num - num//2, middle_num + num//2 + 1)]
    else:
        answer = [i for i in range(middle_num - num//2+1, middle_num + num//2 + 1)]
    return answer