from sys import path
path.append("../codingtest_prac")
from timecheckers.timechecker import elapsed
from pprint import pprint
'''
https://school.programmers.co.kr/learn/courses/30/lessons/181916
주사위 게임 3


문제 설명

1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 
네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 
q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 
각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 
각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 
얻는 점수를 return 하는 solution 함수를 작성해 주세요.


제한사항

a, b, c, d는 1 이상 6 이하의 정수입니다.


입출력 예
a	b	c	d	result
2	2	2	2	2222
4	1	4	4	1681
6	3	3	6	27
2	5	2	6	30
6	4	2	5	2
'''
'''
1. 구해야 하는 것

2. 1을 구하기 위해 필요한 것

3. 그 외 고려해야 할 사항
'''
args = [6,4,2,5] # "result" : 2
# args = [2,2,2,2] # "result" : 2222
# args = [4,1,4,4] # "result" : 1681
# args = [6,3,3,6] # "result" : 27
# args = [2,5,2,6] # "result" : 30



point = 0
ds = list(set(args))
if len(set(args)) == 1:
    point += int(f"{args[0]}{args[0]}{args[0]}{args[0]}")
elif len(set(args)) == 2:
    if args.count(ds[0]) == 2:
        point += (ds[0] + ds[1]) * abs(ds[0] - ds[1])
    elif args.count(ds[0]) == 1 and args.count(ds[1]) == 3:
        point += (10*ds[1] + ds[0])**2
    else:
        point += (10*ds[0] + ds[1])**2

elif len(set(args)) == 3:
    if args.count(ds[0]) == 2:
        point += ds[1]*ds[2]
    elif args.count(ds[1]) == 2:
        point += ds[0]*ds[2]
    else:
        point += ds[0]*ds[1]        

elif len(set(args)) == 4:
    point += min(args)

print(point)



@elapsed
def solution(*args):
    point = 0
    length = len(set(args))
    ds = list(set(args)) #dice_set

    if length == 1:
        point += int(f"{args[0]}{args[0]}{args[0]}{args[0]}")
    elif length == 2:
        if args.count(ds[0]) == 2:
            point += (ds[0] + ds[1]) * abs(ds[0] - ds[1])
        elif args.count(ds[0]) == 1 and args.count(ds[1]) == 3:
            point += (10*ds[1] + ds[0])**2
        else:
            point += (10*ds[0] + ds[1])**2

    elif length == 3:
        if args.count(ds[0]) == 2:
            point += ds[1]*ds[2]
        elif args.count(ds[1]) == 2:
            point += ds[0]*ds[2]
        else:
            point += ds[0]*ds[1]        

    elif length == 4:
        point += min(args)
    
    return point
print(solution(args))

