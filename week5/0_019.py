'''
https://school.programmers.co.kr/learn/courses/30/lessons/181832
정수를 나선형으로 배치하기


문제 설명
양의 정수 n이 매개변수로 주어집니다. 
n * n 배열에 1부터 n**2 까지 정수를 인덱스 [0][0]부터 
시계방향 나선형으로 배치한 이차원 배열을 return 하는 
solution 함수를 작성해 주세요.

제한사항
1 ≤ n ≤ 30
'''

n = 4


answer = [[0]*n]*n

# 1씩 늘려가면서 넣기
# index out of range 나오면 어떻게 방향을 돌려버려
# 계속 돌려버려

for i in range(1,n**2+1):
    pass
