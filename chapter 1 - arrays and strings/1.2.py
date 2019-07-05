def check_permutation(str1, str2):
    if len(str1) != len(str2):
        # stop if length not equal
        return False

    char_dict = {}
    for char in str1:
        if char_dict.get(char):
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for char in str2:
        if char_dict.get(char):
            char_dict[char] -= 1
        else:
            # one char missing then stop
            return False
    return True


if __name__ == "__main__":
    result = check_permutation("aabcdbsccba", "aabcdbscacb")
    print(result)

