# -*- coding: utf-8 -*-
# https://ac.nowcoder.com/acm/contest/49/G
inf = 0x3f3f3f3f
maxn = 501
dirx = [0, 1, -1, 0]
diry = [1, 0, 0, -1]
global n, m


def init():
    global flag
    flag = True
    global maze
    maze = []
    global sx, sy, ex, ey
    for i in range(n):
        maze.append(input())
        for j in range(m):
            if maze[i][j] == 'S':
                sx = i
                sy = j
            elif maze[i][j] == 'E':
                ex = i
                ey = j


def cal(sx, sy):
    global flag
    queue = []
    queue.append((sx, sy))
    while queue:
        q = queue[0]
        if q[0] == ex and q[1] == ey:
            print('Yes')
            flag = False
            break
        queue.pop(0)
        for i in range(4):
            nx = q[0] + dirx[i]
            ny = q[1] + diry[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] != '#':
                    queue.append((nx, ny))
                    maze[nx] = list(maze[nx])
                    maze[nx][ny] = '#'
                    maze[nx] = ''.join(maze[nx])

    if flag:
        print('No')


if __name__ == '__main__':
    try:
        while True:
            n, m = map(int, input().split())
            init()
            cal(sx, sy)
    except EOFError:
        pass
