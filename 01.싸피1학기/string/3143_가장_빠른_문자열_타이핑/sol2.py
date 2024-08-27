A = 'bcbcbcbcbcbcbcbc'
B = 'bc'

cnt = 0

for i in range(len(A)):
    if i + len(B) <= len(A) and A[i:i + len(B)] == B:
        cnt += 1

C = len(A) - (len(B) * cnt)
print(f'{cnt + C}')