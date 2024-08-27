import sys
sys.stdin = open('input.txt')


#테스트케이스가 10번 주어지므로 10번 반복한다
for test in range(10) :
    N = int(input())
    arr = list(map(int, input().split()))

    #시야가 확보된 세대수를 변수 apt로 지정한다
    #제일 처음은 0이다
    apt = 0
    #가장 왼쪽 두 건물은 왼쪽 조망이 확보되지 않고 가장 오른쪽 두 건물은 오른쪽 조망이 확보되지 않기에
    #그 네 건물을 뺀 나머지 건물들을 살펴본다
    for i in range(2, N-2) :
        #인덱스 i 건물이 양 옆의 네 건물보다 높은지 확인할 변수 check
        check = 0
        #건물 높이를 임시로 저장할 리스트 temp
        temp = []

        #인덱스 i 건물의 왼쪽에 있는 두 건물과 오른쪽에 있는 두 건물을 살펴본다
        for j in range(i-2, i+3) :
            #만약 i 건물이 다른 건물들보다 더 높다면
            if arr[i] > arr[j] :
                #temp 리스트에 i 건물에서 다른 건물의 높이를 뺀 값(차이)을 추가하고
                temp.append(arr[i] - arr[j])
                #check 변수에 1을 더한다
                check += 1

            #왼쪽과 오른쪽의 조망이 확보되려면 인덱스 i의 건물이 가장 높아야 한다
            #range(i-2, i+3)에서 자기 자신을 빼고 네 개의 건물이 i 건물보다 높이가 낮다면
            if check == 4:
                #임시로 i 건물과 가장 적은 높이 차이(min)를 temp[0]에 있는 값으로 지정한다
                min = temp[0]
                #temp의 값을 반복하면서
                for num in temp:
                    #min보다 작은 값이 있다면(i 건물이랑 높이 차이가 덜 나는 건물이 있음)
                    if min > num:
                        #그 값을 min에 대입한다
                        min = num
                #가장 높이 차이가 적게 나는 값이 아파트 조망권 확보한 세대의 수다
                #변수 apt에 조망권을 확보한 세대의 수를 더한다
                apt += min

    #test는 인덱스 0부터 시작되기에 1을 더한다
    print(f'#{test+1} {apt}')