import sys
sys.stdin = open('input.txt')

T = int(input())

num = {'ZRO': 0,
       'ONE': 1,
       'TWO': 2,
       'THR': 3,
       'FOR': 4,
       'FIV': 5,
       'SIX': 6,
       'SVN': 7,
       'EGT': 8,
       'NIN': 9
       }

lan = {0: 'ZRO',
       1: 'ONE',
       2: 'TWO',
       3: 'THR',
       4: 'FOR',
       5: 'FIV',
       6: 'SIX',
       7: 'SVN',
       8: 'EGT',
       9: 'NIN'
       }

for tc in range(1, T+1) :
    N, M = input().split()
    arr = list(input().split())

    for i in range(int(M)) :
        for j in num.keys():
            if arr[i] == j :
                arr[i] = num[j]

    arr.sort()

    for i in range(int(M)) :
        for j in lan.keys():
            if arr[i] == j :
                arr[i] = lan[j]
    print(N)
    print(*arr)





