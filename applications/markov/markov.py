import random, re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

following = {}

prev = None
for word in words.split():
    if prev is None:
        prev = word
    elif prev not in following:
        following[prev] = [word]
        prev = word
    else:
        following[prev].append(word)
        prev = word


# TODO: construct 5 random sentences
# Your code here

# if word begins with capital letter, it is the start of a sentance
# if the word ends in punctuation, it is a sentance.
sentance = ""
counter = 0
start = []

for k, v in following.items():
    if k[0].isupper() or re.match("\"", k[0]):
        start.append(k)

while counter < 5:
    beginning = random.choice(start)
    print(beginning, end=" ")
    stop = False

    while stop == False:
        next_word = random.choice(following[beginning])

        if re.match(".?!", next_word[-1]) is None:
            print(next_word, end=" ")
            beginning = next_word
            stop = False
            continue
        else:
            print(next_word, "\n")
            counter += 1
            stop = True
