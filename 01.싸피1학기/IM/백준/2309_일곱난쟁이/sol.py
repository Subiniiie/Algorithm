arr = ['o', 'x']
path = []
nanjeang = [int(input()) for _ in range(9)]

temp = []
def print_nanjeang() :
    global result
    if path.count('o') == 7 :
        for i in range(9) :
            if path[i] == 'o' :
                temp.append(nanjeang[i])


def run(lev) :
    if lev == 9 :
        print_nanjeang()
        return

    for i in range(2) :
        path.append(arr[i])
        run(lev + 1)
        path.pop()

run(0)

result = []
for i in range(len(temp) - 7) :
    if sum(temp[i:i+7]) == 100 :
        result = temp[i:i+7]
        break

result.sort()
for i in range(len(result)) :
    print(result[i])