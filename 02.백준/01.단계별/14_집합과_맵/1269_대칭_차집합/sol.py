import sys
A, B = map(int, sys.stdin.readline().split())
A_lst = list(map(int, sys.stdin.readline().split()))
B_lst = list(map(int, sys.stdin.readline().split()))

A_set = set(A_lst)
B_set = set(B_lst)

difference_1 = A_set - B_set
difference_2 = B_set - A_set
result = difference_1 | difference_2
print(len(result))


