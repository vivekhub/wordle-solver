#!/usr/bin/env python
import random
import sys

WORDS = []


def init_words(words=None):
    global WORDS
    WORDS = words if words else []


def load_dictionary():
    global WORDS
    init_words()
    with open("five.txt", "r") as f:
        item = 1
        w = f.readline().strip()
        while w:
            WORDS.append(w)
            w = f.readline().strip()
            item += 1


def prune_position_match(letter, position):
    global WORDS
    WORDS = list(filter(lambda w: w[position] == letter, WORDS))


def prune_letters(letters):
    global WORDS
    new_words = set(WORDS)
    for letter in letters:
        new_words = set(filter(lambda x: letter in x, new_words))

    if new_words:
        init_words(list(new_words))


def prune_notexist(letters):
    global WORDS
    new_words = set(WORDS)
    for letter in letters:
        new_words = set(filter(lambda x: letter not in x, new_words))
    if new_words:
        init_words(list(new_words))


def process_resp(word, resp, solution):
    letters_match = []
    wrong_letter = []
    global WORDS

    if resp == "ggggg":
        # We solved it
        WORDS = [
            word,
        ]
        return True

    # Remove this word
    WORDS = list(filter(lambda x: word != x, WORDS))

    for i, letter in enumerate(resp):
        if letter == "g":
            prune_position_match(word[i], i)
            if solution and solution not in WORDS:
                print(f"BUG!, pruning of {word[i]} in position{i}")

        elif letter == "y":
            letters_match.append(word[i])
        else:
            wrong_letter.append(word[i])

    prune_letters(letters_match)
    if solution and solution not in WORDS:
        print(f"BUG!, pruning of {letters_match}")

    prune_notexist(wrong_letter)
    if solution and solution not in WORDS:
        print(f"BUG!, pruning of deleted words {wrong_letter}")

    return len(WORDS) == 1


def achoice(solution=None):
    attempt = 1
    tryword = "raise"
    while attempt < 7:
        resp = input(f"Try the word {tryword} ==>")
        resp = resp.lower()

        found = process_resp(tryword, resp, solution)
        if found:
            print(f"The word is : {WORDS[0]}")
            return

        if len(WORDS) < 20:
            print(f"The word is one of : {WORDS}")
        else:
            print(f"We have {len(WORDS)} choices")
        attempt += 1
        tryword = random.choice(WORDS)
    print(f"We couldnt figure out from this list  : {WORDS}")


def main(debug=False):
    load_dictionary()
    print(f"We have {len(WORDS)} dictionary words")
    if debug:
        solution = input("enter the solution:")
        achoice(solution)
    else:
        achoice()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--debug":  # Yeah I know about argparse
            main(debug=True)
            sys.exit(1)
    print("As I prompt you with words, reply back with the following response")
    print("b = black")
    print("g = green")
    print("y = yellow")
    print('For example if the word is "bring"  and the guess is "orate"')
    print('Reply with "bgbbb"')
    main()
    sys.exit(0)
