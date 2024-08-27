import sys
N = int(sys.stdin.readline())
dict = {}
lst = []

for _ in range(N) :
    word = sys.stdin.readline().rstrip()
    if len(word) in dict :
        if word in dict[len(word)] :
            pass
        else :
            dict[len(word)].append(word)
    else :
        dict[len(word)] = [word]
        lst.append(len(word))

lst.sort()

for digit in lst :
    if digit in dict :
        dict[digit].sort()
        for i in range(len(dict[digit])) :
            print(dict[digit][i])