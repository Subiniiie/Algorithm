arr = list(input().split())

alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''
num = int(arr[0])

while num > 0 :
    remainder = num % int(arr[1])
    result += alpha[remainder]
    num = num // int(arr[1])

print(result[::-1])