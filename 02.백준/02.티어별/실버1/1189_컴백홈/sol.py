import sys

R, C, K = map(int, sys.stdin.readline().split())

arr = []
for _ in range(R) :
    arr.append(list(sys.stdin.readline().strip()))


drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]


def dfs(row, col) :
    global result
    if row == 0 and col == C - 1 :
        if arr[row][col] == K :
            result += 1
            return
        else :
            return

    if row <= -1 or row >= R or col <= -1 or col >= C :
        return
    else :
        for i in range(4) :
            temp_row = row + drow[i]
            temp_col = col + dcol[i]
            if 0 <= temp_row < R and 0 <= temp_col < C :
                if arr[temp_row][temp_col] == '.' :
                    arr[temp_row][temp_col] = arr[row][col] + 1
                    dfs(temp_row, temp_col)
                    arr[temp_row][temp_col] = '.'


result = 0
arr[R - 1][0] = 1

dfs(R - 1, 0)
print(result)

