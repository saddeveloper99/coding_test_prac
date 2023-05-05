'''
https://school.programmers.co.kr/learn/courses/30/lessons/12906
같은 숫자는 싫어

문제 설명
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 
이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 
하나만 남기고 전부 제거하려고 합니다. 단, 제거된 후 남은 수들을 
반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 
return 하는 solution 함수를 완성해 주세요.

제한사항
배열 arr의 크기 : 1,000,000 이하의 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

 
'''
# arr = [1,1,3,3,0,1,1] # [1,3,0,1]
arr = [4,4,4,3,3]
'''
1. 구해야 하는 것
    연속적으로 나타나는 숫자를 하나만 남기고 제거한 배열
2. 1을 구하기 위해 필요한 것
    # 중복 판별하는 방법
        # index순으로 다음 인덱스의 값과 비교
    # 중복 제거하는 방법
        # 같으면 del
3. 그 외 고려해야 할 사항
    # 삭제하면 인덱스 에러 발생
'''
a = []
for i in arr:
    a.append(i)
    try:
        if a[-1] == a[-2]:
            a.pop()
    except:
        continue
print(a)



# 제출용 함수
def solution(arr):
    answer = []
    for i in arr:
        a.append(i)
        try:
            if a[-1] == a[-2]:
                a.pop()
        except:
            continue
    return answer

# print(solution(arr))

