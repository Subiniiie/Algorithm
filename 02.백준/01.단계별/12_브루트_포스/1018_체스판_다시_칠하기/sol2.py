N, M = map(int, input().split())
arr = [[ i for i in input()] for _ in range(N)]

result = 50 * 50 + 1
for x in range(N-7):
    for y in range(M-7):
        temp_b = 0
        temp_w = 0
        for w in range(x, x+8):
            for h in range(y, y+8):
                if w % 2 == 0 and h % 2 == 0 :
                    if arr[w][h] == 'W':
                        temp_b += 1
                    else :
                        temp_w += 1
                elif w % 2 == 0 and h % 2 != 0 :
                    if arr[w][h] == 'B':
                        temp_b += 1
                    else :
                        temp_w += 1
                elif w % 2 != 0 and h % 2 == 0 :
                    if arr[w][h] == 'B':
                        temp_b += 1
                    else :
                        temp_w += 1
                elif w % 2 != 0 and h % 2 != 0 :
                    if arr[w][h] == 'W':
                        temp_b += 1
                    else :
                        temp_w += 1
        result = min(result, temp_b, temp_w)
print(result)