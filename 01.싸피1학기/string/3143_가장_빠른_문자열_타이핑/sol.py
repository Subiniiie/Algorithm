import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    A, B = input().split()

    cnt = 0

    for i in range(len(A)) :
        if i + len(B) <= len(A) and A[i:i+len(B)] == B:
                cnt += 1

    C = len(A) - (len(B) * cnt)
    print(f'#{tc} {cnt + C}')


