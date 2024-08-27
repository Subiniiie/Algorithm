import sys
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check_cards = list(map(int, sys.stdin.readline().split()))
set_cards = set(cards)

for card in check_cards :
    if card in set_cards :
        print(1, end=" ")
    else :
        print(0, end=" ")
