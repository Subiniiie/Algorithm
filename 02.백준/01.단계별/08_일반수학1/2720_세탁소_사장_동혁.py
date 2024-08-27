T = int(input())
for tc in range(1, T+1) :
    C = int(input())

    money = {'Q': 25, 'D': 10, 'N': 5, 'P':1}
    result = {'Q':0, 'D': 0, 'N': 0, 'P': 0}

    while C > 0 :
        if C >= money['Q'] :
            C = C - money['Q']
            result['Q'] += 1
        elif C >= money['D'] :
            C = C - money['D']
            result['D'] += 1
        elif C >= money['N'] :
            C = C - money['N']
            result['N'] += 1
        else :
            C = C - money['P']
            result['P'] += 1

    print(*result.values())
