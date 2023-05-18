'''
https://school.programmers.co.kr/learn/courses/30/lessons/12921
소수 찾기

문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, 
solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
'''

# 4
'''
1. 구해야 하는 것
    # 1부터 n사이의 소수
2. 1을 구하기 위해 필요한 것
    # 소수를 구하는 방법
        # 에라토스테네스의 체
        # 직접 나눠서 세기(제곱근까지)
        # 라이브러리 사용
3. 그 외 고려해야 할 사항
'''
# count = 0
# answer = 0
# for i in range(3, n+1):  # 1부터 n까지
#     for j in range(2, int(i ** 0.5) + 1):  # 2부터 i의 제곱근+1까지로 각각 나눠보면서 나머지가 0이면 약수임
#         if i % j == 0:
#             count += 1
#     if count == 0:
#         answer += 1
#     count = 0
# print(answer+1)

# 제출용 1(시간 초과;;;;;;;;;;;;)
def solution(n):
    count = 0
    answer = 0
    for i in range(3, n+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
        if count == 0:
            answer += 1
        count = 0
    return answer + 1



###########################################################################################################################################################################
# 에라토스테네스의 체
#
# 핵심은 소수의 배수를 지워나가는 것.
# 2부터 시작해서 2 4 6 8 ... 을 지우고
# 다음 소수인 3의 배수 3 9 15 ...을 지우고(6과 12는 앞에서 이미 지워짐)
# ...
# 결국 소수만 남는다.

n = 20
# 0부터 n까지 인덱스로 표현할 배열 생성
# (인덱스 매칭의 편의성을 위해 n+1개)
numbers = [True]*(n+1)  # True면 소수, 소수로 나눠지면 False로 바꿔줄 예정

# 0과 1은 소수가 아님
numbers[0], numbers[1] = False, False

# 2부터 n까지 돌면서(n의 제곱근까지만 돌아도 ok)
for i in range(2, int(n ** 0.5) + 1):
    if numbers[i]==True:  # 특정 수가 지워지지 않았다면 (소수여서)
        k = 2  # i * 1은 자기자신(소수)이므로 2부터 시작

        # i의 배수를 지워주는 작업 i*2 i*3 i*4 ... n이하의 모든 배수를 지워준다.
        while (i * k) <= n:  # i * k가 n보다 커질때까지 반복
            numbers[i*k] = False
            k += 1

for i in range(len(numbers)):
    if numbers[i]:
        print(i, end=' ')



# 왜 제곱근까지만 해도 되는지?
# n = 144(12*12)일 때, 12까지만 확인해도 된다는 뜻

# 2 4 6 8 ...
# 3 9 15 21 ...
# 4 pass (4는 False이므로)
# 5 25(5*5) 35(5*7) 55(5*11) ...
# 6 pass
# 7 49(7*7) 77(7*11)
# 8 pass
# 9 pass
# 10 pass
# 11 11*11 11*13 / 11*17 ...

# 해당 수보다 작은 소수와의 곱은 이전에 모두 지워지게 된다 ex)3*7은 3에서 다 지워져서 7에서는 고려할 필요가 없음
# 따라서 자신보다 큰 소수와의 곱만 지워주면 된다. 따라서 제곱근까지만 판별하면 소수를 모두 판별할 수 있다.


def solution(n):
    numbers = [True]*(n+1)
    numbers[0], numbers[1] = False, False


    for i in range(2, int(n ** 0.5) + 1):
        if numbers[i]:
            k = 2

            while (i * k) <= n:
                numbers[i*k] = False
                k += 1
    return numbers.count(True)

# print(solution(n))


def solution(n):
    num=set(range(2,n+1)) 

    for i in range(2,int(n ** 0.5) + 1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

