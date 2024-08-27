T = int(input())
for tc in range(T) :
    N, arr = map(str, input().split())

    str_result = ''
    for i in range(len(arr)) :
        str_result = str_result + arr[i] * int(N)

    print(str_result)
