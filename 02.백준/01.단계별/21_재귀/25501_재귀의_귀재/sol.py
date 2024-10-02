import sys
T = int(sys.stdin.readline().rstrip())


def recursion(s, l , r) :
    global cnt
    if l >= r :
        return 1
    else :
        if s[l] != s[r] :
            return 0
        else :
            cnt += 1
            return recursion(s, l + 1, r - 1)


def isPalindrome(s, l, r) :
    return recursion(s, l, r)

for _ in range(T) :
    S = sys.stdin.readline().rstrip()
    cnt = 1

    print(isPalindrome(S, 0, len(S) - 1), cnt)

