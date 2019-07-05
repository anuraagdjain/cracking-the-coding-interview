def substring(a, b):
    return b in a


def string_rotation(a, b):
    if len(a) == len(b):
        return substring(a + a, b)
    else:
        return False


if __name__ == "__main__":
    words = [["waterbottle", "erbottlewat"], ["ABACD", "CDAZBA"], ["ABACD", "CDABA"]]
    for word in words:
        print(string_rotation(word[0], word[1]))
