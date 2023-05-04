'''
https://school.programmers.co.kr/learn/courses/30/lessons/120861
캐릭터의 좌표


문제 설명

머쓱이는 RPG게임을 하고 있습니다. 
게임에는 up, down, left, right 방향키가 있으며 
각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
예를 들어 [0,0]에서 캐릭터의 좌표는 
up을 누른다면 [0, 1], 
down을 누른다면 [0, -1], 
left를 누른다면 [-1, 0], 
right를 누른다면 [1, 0]입니다. 
머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 
캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.


제한사항

board은 [가로 크기, 세로 크기] 형태로 주어집니다.
board의 가로 크기와 세로 크기는 홀수입니다.
board의 크기를 벗어난 방향키 입력은 무시합니다.
0 ≤ keyinput의 길이 ≤ 50
1 ≤ board[0] ≤ 99
1 ≤ board[1] ≤ 99
keyinput은 항상 up, down, left, right만 주어집니다.

'''
# keyinput = ["left", "right", "up", "right", "right"]
# board = [11, 11]

keyinput = ["down", "down", "down", "down", "down"]
board = [7, 9]


def solution(keyinput, board):
    position = [0, 0]
    for direction in keyinput:
        if direction == "right":
            if position[0] == board[0]//2:
                pass
            else:
                position[0] += 1

        elif direction == "left":
            if position[0] == -board[0]//2+1:
                pass
            else:
                position[0] -= 1

        elif direction == "up":
            if position[1] == board[1]//2:
                pass
            else:
                position[1] += 1

        elif direction == "down":
            if position[1] == -board[1]//2+1:
                pass
            else:
                position[1] -= 1
    return position


def solution(keyinput, board):
    x, y = 0, 0
    for direction in keyinput:
        if direction == "right":
            x = min(x + 1, board[0]//2)
        elif direction == "left":
            x = max(x - 1, -board[0]//2 + 1)
        elif direction == "up":
            y = min(y + 1, board[1]//2)
        elif direction == "down":
            y = max(y - 1, -board[1]//2 + 1)
    return [x, y]



print(solution(keyinput, board))


# a = -7
# print(a // 2) 