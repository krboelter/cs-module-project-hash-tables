def no_dups(s):
    words = s.split()
    word_dict = {}

    for word in words:
        word_dict[word] = 1

    answer = []
    for k in word_dict.keys():
        answer.append(k)

    return answer




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
