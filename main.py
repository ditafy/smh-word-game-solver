from loader import load_words
from collections import Counter

#load word list
#words_3000 = load_words("data/Oxford 3000.txt")
#words_extra = load_words("data/Oxford 5000.txt")
#word_list = list(set(words_3000 + words_extra))
word_list = load_words('data/words.txt')


#test input
letters = ['r', 'i', 'y', 'i', 'e', 'w', 'f', 'd', 'm']
center = 'e'
if center not in letters:
    raise ValueError("Center letter must be included in letters")

letter_count = Counter(letters)

def is_valid_word(word, letter_count, center):
    #length >=4
    if len(word) < 4:
        return False

    #include center word
    if center not in word:
        return False

    #filter s
    if word.endswith('s'):
        return False

    #usage
    word_count = Counter(word)

    for char in word_count:
        if word_count[char] > letter_count.get(char, 0):
            return False

    return True

#collect valid words
valid_words = []

for word in word_list:
    if is_valid_word(word, letter_count, center):
        valid_words.append(word)

print("Valid words:")
print(valid_words)
