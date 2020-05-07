word1 = input()
word2 = input()

# How many letters does the longest word contain?

word1_len = len(word1)
word2_len = len(word2)

print(max(word1_len, word2_len))
