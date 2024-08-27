import sys
import math
D, H, W = map(int, sys.stdin.readline().split())

z = math.sqrt((H ** 2) + (W ** 2))
print(math.floor(H * (D / z)), math.floor(W * (D / z)))

