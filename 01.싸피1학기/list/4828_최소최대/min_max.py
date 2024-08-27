import sys
sys.stdin = open('sample_input.txt')

#제일 처음 값은 문제의 개수
T = int(input())

for t in range(T) :
    #리스트에 있는 값의 개수
    N = int(input())
    arr = list(map(int, input().split()))
    #max와 min을 구해야해서 제일 처음 비교값 설정
    max = 0
    min = 1000000
    #리스트 arr를 반복하며 값을 비교한다
    for num in arr :
        #num이 max보다 크면 max는 num이다
        if max < num :
            max = num
        #num이 min보다 작으면 min은 num이다
        if min > num :
            min = num


    print(f'#{t+1} {max - min}')
