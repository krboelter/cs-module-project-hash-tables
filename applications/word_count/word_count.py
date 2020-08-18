import re

def word_count(s):
    # Your code here
    words = {}
    for word in s.lower().split():
        # n = re.sub("[^a-zA-z']+", "", word)
        # n = "".join(filter(str.isalnum, word))
        n = "".join(re.sub("[^a-zA-Z']+", "", word))
        if n not in words:
            words[n] = 1
        else:
            words[n] += 1

    if "" in words:
        return {}
    else:
        return words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
