import time
'''
https://school.programmers.co.kr/learn/courses/30/lessons/181851
전국 대회 선발 고사


문제 설명

0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다.
등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이
있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.

각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 
담긴 boolean 배열 attendance가 매개변수로 주어집니다. 전국 대회에 선발된 학생 
번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 
10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.


제한사항

3 ≤ rank의 길이 = attendance의 길이 ≤ 100
rank[i]는 i번 학생의 선발 고사 등수를 의미합니다.
rank의 원소는 1부터 n까지의 정수로 모두 서로 다릅니다.
attendance[i]는 i번 학생의 전국 대회 참석 가능 여부를 나타냅니다.
attendance[i]가 true라면 참석 가능, false면 참석 불가능을 의미합니다.
attendance의 원소 중 적어도 3개는 true입니다.

 
'''
rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]
'''
1. 구해야 하는 것
    # 참여가능한 학생 등수 순으로 3명
    # 10000 * a + 100 * b + c
2. 1을 구하기 위해 필요한 것
    # 등수먼저 뽑고 참여여부를 비교?
        # min()으로 1등부터 뽑아온다. or 
            # index()로 인덱스를 알아낸다.
        # attendance에서 인덱스 비교
        # true면 계산에 더해준다
3. 그 외 고려해야 할 사항
'''

result = []
for i in range(len(rank)):
    # print(rank.index(i+1))
    index = rank.index(i+1) # 1등부터 차례대로 몇번째 인덱스에 있는지 
    # print(index)
    if attendance[index]: # True면
        result.append(index) # 해당 학생의 인덱스를 result에 추가
        # print(result)
        if len(result) == 3: # 3등까지 뽑았다면 결과계산
           print(result[0]*10000 + result[1]*100 + result[2])
           break


def solution(rank, attendance):
    result = []
    for i in range(len(rank)):
        index = rank.index(i+1)
        if attendance[index]:
            result.append(index)
            if len(result) == 3:
                answer = result[0]*10000 + result[1]*100 + result[2]
                return answer

# print(solution())


arr = [i for i in range(1, 100000000)]
att = [True]*len(arr)

a = time.time()

print(solution(arr, att))

print("걸린 시간 : ", time.time() - a)