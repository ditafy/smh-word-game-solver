from loader import load_words
from collections import Counter, defaultdict

#load word list
#words_3000 = load_words("data/Oxford 3000.txt")
#words_extra = load_words("data/Oxford 5000.txt")
#word_list = list(set(words_3000 + words_extra))
word_list = load_words('data/en_AU-large.txt')


def get_user_input():
    letters_input = input("Enter 9 letters separated by spaces: ").strip().lower()
    letters = letters_input.split()

    if len(letters) != 9:
        raise ValueError("You must enter exactly 9 letters.")

    if not all(len(letter) == 1 and letter.isalpha() for letter in letters):
        raise ValueError("Each entry must be a single letter.")

    center = input("Enter the center letter: ").strip().lower()

    if len(center) != 1 or not center.isalpha():
        raise ValueError("Center letter must be a single letter.")

    if center not in letters:
        raise ValueError("Center letter must be included in letters.")

    return letters, center


letters, center = get_user_input()

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

words_by_length = defaultdict(list)

for word in valid_words:
    words_by_length[len(word)].append(word)

print("Valid words by length:")

for length in sorted(words_by_length):
    print(f"\n{length}-letter words ({len(words_by_length[length])}):")
    print(sorted(words_by_length[length]))
