# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 여행 경로
# Prgrammers / Level 3

res = []


def bfs(start, depth, ways, tickets, visited):
    if depth == len(tickets):
        temp_ways = []
        for way in ways:
            temp_ways.append(way)
        temp_ways.append(start)
        res.append(temp_ways)
        return

    for i in range(len(tickets)):
        if visited[i]:
            continue
        if tickets[i][0] == start:
            visited[i] = True
            ways.append(start)
            bfs(tickets[i][1], depth+1, ways, tickets, visited)
            visited[i] = False
            ways.pop()

def solution(tickets):
    visited = [False for _ in range(len(tickets))]
    bfs("ICN", 0, [], tickets, visited)
    res.sort() # 알파벳 순 정렬
    return res[0]


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
solution(tickets)