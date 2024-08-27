x, y, w, h = map(int, input().split())

m = 1001
if m > abs(w - x) :
    m = abs(w - x)
if m > abs(0 - x) :
    m = abs(0 - x)
if m > abs(h - y) :
    m = abs(h - y)
if m > abs(0 - y) :
    m = abs(0 - y)
print(m)