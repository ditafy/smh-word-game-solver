def load_words(file_path):
    words = []

    with open(file_path, "r") as f:
        for line in f:
            word = line.strip().lower()

            if word.isalpha():
                words.append(word)

    return words