def string_compression(_str):
    idx = 0
    result = ""
    str_length = len(_str)
    while idx < str_length and _str[idx] != None:
        curr_char = _str[idx]
        ctr = 1
        idx += 1
        if idx != str_length:
            while curr_char == _str[idx]:
                ctr += 1
                idx += 1
                if idx == str_length:
                    break
        result += curr_char + "" + str(ctr)
    return result if len(result) < len(_str) else _str


if __name__ == "__main__":
    words = [
        "aabcccccaaa",
        "abcd",
        "aaabaaaaccaaaaba",
        "aabccddeeaa",
        "aaaabbccccdddeee",
        "AAABBBBCC",
    ]
    # print(string_compression("aabcccccaaa"))
    for word in words:
        print(string_compression(word))
