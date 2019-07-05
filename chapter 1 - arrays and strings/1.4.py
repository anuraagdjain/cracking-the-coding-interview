def permutation_palindrome(_str):
    str = _str.strip()
    char_map = {}
    for char in str:
        char_map[char] = char_map[char] + 1 if char_map.get(char) else 1
    odd = 0
    for value in char_map.values():
        if value % 2 != 0:
            odd += 1
    return False if odd > 1 else True


if __name__ == "__main__":
    words = ["never odd or even", "racer car"]
    for word in words:
        result = permutation_palindrome(word)
        print(result)
