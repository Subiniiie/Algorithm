import sys

arr = []
while 1 :
    temp = sys.stdin.readline().rstrip()
    if temp == "." :
        break
    else :
        for n in temp :
            if n == "(" or n == "[" :
                arr.append(n)
            elif n == ")" :
                if "(" in arr and arr[-1] == "(" :
                    del arr[-1]
                else :
                    break
            elif n == "]" :
                if "[" in arr and arr[-1] == "[":
                    del arr[-1]
                else :
                    break
        if n not in ["[", "]", "(", ")"] and len(arr) == 0 :
            print('yes')
        else :
            print('no')
        arr = []
