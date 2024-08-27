munja = {'ABC': 2,
        'DEF' : 3,
        'GHI' : 4,
        'JKL' : 5,
        'MNO' : 6,
        'PQRS' : 7,
        'TUV' : 8,
        'WXYZ' : 9}

alpha = input()

lst = []
for i in alpha :
    for key in munja.keys() :
        if i in key :
            lst.append(munja[key])

result = 0
for i in lst :
    result += (i + 1)
print(result)


