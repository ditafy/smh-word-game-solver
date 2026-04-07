# SMH Word Game

## Overview
A solver for word game Target

## How the game works
- Create as many words as you can to complete all 4 targets.
    - Find words of four letters or more.
    - Every word must include the centre letter and each letter is used once only.
    - Find at least one nine-letter word.
    - No colloquial or foreign words, capitalised nouns, apostrophes, hyphens.
    - No verbs or plural words ending in 's'.


## Data Source
This project currently uses the `en_AU-large` English word list from SCOWL / Aspell:
https://wordlist.aspell.net/

The raw word list is filtered in code to better match the game rules by removing:
- words shorter than four letters
- capitalised words and acronyms
- words containing apostrophes, hyphens, or other non-alphabetic characters
- duplicate entries

The dataset is used for educational and non-commercial purposes.
