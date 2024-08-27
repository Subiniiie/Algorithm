# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# lst = [[16, 15, 14, 13, 0], [12, 11, 10, 9, 0], [8, 7, 6, 5, 0], [4, 3, 2, 1, 0], [0, 0, 0, 0 ,0]]
#
# for i in range(4) :
#     for j in range(4) :
#         lst[arr[i][j]] = 0
# print(lst)

mc = []
for _ in range(5) :
    mc.extend(list(map(int, input().split())))
print(mc)