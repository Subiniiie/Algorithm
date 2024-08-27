arr = []
N = int(input())
for k in range(N):
     i = int(input())
     if k == 0 :
         arr.append(i)
     else :
         if i < arr[0] :
             arr.insert(0, i)
         elif i > arr[len(arr) - 1] :
             arr.append(i)
         else :
             for j in range(len(arr) - 1) :
                 if arr[j] < i < arr[j+1]:
                     arr.insert(j+1, i)

for i in range(len(arr)):
    print(arr[i])