'''
https://school.programmers.co.kr/learn/courses/30/lessons/178871
달리기 경주

문제 설명

얀에서는 매년 달리기 경주가 열립니다. 
해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 
추월한 선수의 이름을 부릅니다. 예를 들어 
1등부터 3등까지 "mumu", "soe", "poe" 선수들이 
순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 
2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 
즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 
문자열 배열 players와 해설진이 부른 이름을 담은 
문자열 배열 callings가 매개변수로 주어질 때, 
경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로
 배열에 담아 return 하는 solution 함수를 완성해주세요.

제한사항
5 ≤ players의 길이 ≤ 50,000
players[i]는 i번째 선수의 이름을 의미합니다.
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
players에는 중복된 값이 들어가 있지 않습니다.
3 ≤ players[i]의 길이 ≤ 10
2 ≤ callings의 길이 ≤ 1,000,000
callings는 players의 원소들로만 이루어져 있습니다.
경주 진행중 1등인 선수의 이름은 불리지 않습니다.


 
'''
players = ["mumu", "soe", "poe", "kai", "mine"] 
callings = ["kai", "kai", "mine", "mine"]
# ["mumu", "kai", "mine", "soe", "poe"]

def solution(players, callings):
    players_dict = {}
    for i, j in enumerate(players):
        players_dict[j] = i
    for i in callings:
        a = players_dict[i]
        cur = players[a]
        pre = players[a-1]
        players_dict[cur] -= 1
        players_dict[pre] += 1

        players[a] = players[a-1]
        players[a-1] = cur
    answer = players
    return answer


# {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
players_dict = {}
# reversed_dict = {}
for i, j in enumerate(players):
    players_dict[j] = i
    # reversed_dict[str(i)] = j
    

for i in callings:
    a = players_dict[i] # 현재 순위
    cur = players[a] # 해당 순위의 선수
    pre = players[a-1]
    players_dict[cur] -= 1
    players_dict[pre] += 1

    players[a] = players[a-1]
    players[a-1] = cur
print(players)



#     a = list(players_dict.keys())[players_dict[i]-1]
#     players_dict[i] -= 1
#     players_dict[a] += 1


#########################################

# for i in players:
#     a = players.index(i)
#     b = callings.count(i)

#     players.insert(a-b, players.pop(a))
# call_set = set(callings)

# # min_idx, max_idx
# for i in call_set:
    


# for i in callings:
#     a = players.index(i)
#     del players[a]
#     players.insert(a-1, i)
# answer = players



# for i in callings:
#     pass


# print(players)

# def solution(players, callings):
#     for i in callings:
#         players.insert(players.index(i)-1, players.pop(players.index(i)))
#     return players

# print(solution())
# print()
