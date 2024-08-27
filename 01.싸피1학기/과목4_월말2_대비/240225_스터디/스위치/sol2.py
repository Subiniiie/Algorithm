switches_num = int(input())
switches = list(map(int, input().split()))
students_num = int(input())
students = [list(map(int, input().split())) for _ in range(students_num)]

switches.insert(0, 0)
for i in range(students_num) :
    if students[i][0] == 1 :
        k = students[i][1]
        s = students[i][1]
        while k <= switches_num :
            if switches[k] == 0 :
                switches[k] = 1
            else :
                switches[k] = 0
            k += s
    else :
        l = students[i][1]
        if switches[l] == 0 :
            switches[l] = 1
        else :
            switches[l] = 0
        w = 1
        while w+l <= switches_num and switches[l-w] == switches[l+w] :
            if l-w == 0 :
                break
            else :
                if switches[l+w] == 0 :
                    switches[l+w] = 1
                    switches[l-w] = 1
                else :
                    switches[l+w] = 0
                    switches[l-w] = 0
            w += 1

for i in range(1, switches_num, 20) :
    print(*switches[i:i+20])


# 20개씩 출력하고 싶을 때
for i in range(1, switches_num, 20) :
    print(switches[i:i+20])