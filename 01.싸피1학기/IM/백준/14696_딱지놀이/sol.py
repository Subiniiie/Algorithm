N = int(input())
arr = [list(map(int, input().split())) for _ in range(2*N)]

for i in range(N) :

    dict_a = {'4': 0, '3': 0, '2': 0, '1': 0}
    dict_b = {'4': 0, '3': 0, '2': 0, '1': 0}

    for key in dict_a.keys():
        for j in range(1, arr[i*2][0]+1) :
            if arr[i*2][j] == int(key) :
                dict_a[key] += 1
        for l in range(1, arr[i*2+1][0]+1) :
            if arr[i*2+1][l] == int(key) :
                dict_b[key] += 1

    if dict_a['4'] > dict_b['4'] :
        print('A')
    elif dict_a['4'] < dict_b['4'] :
        print('B')
    else :
        if dict_a['3'] > dict_b['3']:
            print('A')
        elif dict_a['3'] < dict_b['3']:
            print('B')
        else :
            if dict_a['2'] > dict_b['2']:
                print('A')
            elif dict_a['2'] < dict_b['2']:
                print('B')
            else:
                if dict_a['1'] > dict_b['1']:
                    print('A')
                elif dict_a['1'] < dict_b['1']:
                    print('B')
                else:
                    print('D')

