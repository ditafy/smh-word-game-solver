def load_words(file_path):
    words = []
    seen = set()

    with open(file_path, "r") as f:
        for line in f:
            raw_word = line.strip()

            # Keep only lowercase alphabetic words that fit the game's
            # baseline rules. This removes acronyms, capitalised nouns,
            # apostrophes, hyphens, and very short entries.
            if not raw_word.isalpha():
                continue

            if not raw_word.islower():
                continue

            if len(raw_word) < 4:
                continue

            word = raw_word.lower()

            if word not in seen:
                words.append(word)
                seen.add(word)

    return words
