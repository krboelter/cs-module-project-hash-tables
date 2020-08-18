import re

def histogram(filename):
    word_count = {}
    longest_word = ""
    with open(filename) as file:
        data = file.read()
        file.close()

    for word in re.split('[^A-Za-z0-9]+', data.lower()):
        if len(word) > len(longest_word):
            longest_word = word

        if word.isspace():
            continue
        elif word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return longest_word, {key: value for key, value in sorted(word_count.items(), key=lambda item: item[1], reverse=True)}

longest_word, dictionary = histogram('robin.txt')
for key, val in dictionary.items():
    x = "#" * val
    n = key.ljust(len(longest_word) + 2, " ")
    print(f"{n} {x}")
