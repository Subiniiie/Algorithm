import sys
n = int(sys.stdin.readline())
arr = [0 for _ in range(n)]
students = []
for _ in range(n) :
    students.append(list(map(int, sys.stdin.readline().split())))

for i in range(n-1) :
    for k in range(i+1, n) :
        for j in range(5) :
            if students[i][j] == students[k][j] :
                arr[i] += 1
                arr[k] += 1
                break


s = 0
student = 0
for i in range(n) :
    if s < arr[i] :
        s = arr[i]
        student = i
print(student+1)