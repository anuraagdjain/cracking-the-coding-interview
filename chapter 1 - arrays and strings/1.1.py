def isUnique(str):
    str = str.replace(" ", "")  # remove all spaces
    hash_set = set()  # set to store unique elements
    for char in str:
        if char in hash_set:
            return False
        else:
            hash_set.add(char)
    return True


if __name__ == "__main__":
    print(isUnique("hola"))
