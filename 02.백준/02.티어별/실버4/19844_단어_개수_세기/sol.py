import sys
sentence = sys.stdin.readline().rstrip().replace('-', ' ')
words = sentence.split(' ')

front_word = ("c\'", "j\'", "n\'", "m\'", "t\'", "s\'", "l\'", "d\'", "qu\'", "s\'")
vowels = ("a", "e", "i", "o", "u", "h")

word_cnt = len(words)

for word in words :
    if word.startswith(front_word) :
        apo_idx =word.index("\'")
        apo_next = word[apo_idx+1]

        if apo_next in vowels :
            word_cnt += 1

print(word_cnt)