jumsoo = [list(map(str, input().split())) for _ in range(20)]

gmpj = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
        'C+':2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

hjch = 0
for i in range(20) :
    if jumsoo[i][2] != 'P' :
        hjch += float(jumsoo[i][1])

jggm = 0
for i in range(20) :
    for key in gmpj.keys() :
        if jumsoo[i][2] == key :
            jggm += float(jumsoo[i][1]) * gmpj[key]


print(f'{jggm / hjch:.6f}')