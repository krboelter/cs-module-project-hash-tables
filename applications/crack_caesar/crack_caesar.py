# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
def convert_to_text(file):
    with open(file, "r") as file:
        data = file.read()
        file.close()
    return data

text = convert_to_text("ciphertext.txt")

def frequency(text):
    freq = {}
    total = 0
    for char in text:
        if char.isspace():
            continue
        elif not char.isalpha():
            continue
        elif char in freq:
            total += 1
            freq[char] += 1
        else:
            total += 1
            freq[char] = 1

    for letter, count in freq.items():
        freq[letter] = round(count/total * 100, 2)

    return {key: value for key, value in sorted(freq.items(), key=lambda item: item[1], reverse=True)}



def cipher_text():
    letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    freq = frequency(text)

    count = 0
    for letter, perc in freq.items():
        freq[letter] = letters[count]
        count += 1

    plain_text = ""
    for char in convert_to_text("ciphertext.txt"):
        if char.isspace():
            plain_text += " "
        elif not char.isalpha():
            plain_text += char
        else:
            plain_text += freq[char]

    print(plain_text)

cipher_text()
