while True :
    n = int(input())
    if n == -1 :
        break
    else :
        m = 0
        lst = []
        for i in range(1, n) :
            if n % i == 0 :
                m += i
                lst.append(i)
                lst.append('+')
        if n == m :
            print(n, '=', end=' ')
            for j in range(len(lst)-1) :
                if j != len(lst)-2 :
                    print(lst[j],'', end='')
                else :
                    print(lst[j], end='')

            print(sep='\n')
        else :
            print(n, 'is NOT perfect.')

