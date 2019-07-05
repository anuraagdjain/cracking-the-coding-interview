def one_edit_away(a, b):
    idx1 = 0
    idx2 = 0
    found = False
    while idx1 < len(a) and idx2 < len(b):
        if a[idx1] != b[idx2]:
            if found:
                return False
            found = True
            if len(a) == len(b):
                # when both length are same and one char change
                idx2 += 1
        else:
            # move second pointer
            idx2 += 1
        # move first pointer
        idx1 += 1
    return True


if __name__ == "__main__":
    words = [["pale", "ple"], ["pales", "pale"], ["pale", "bale"], ["pale", "bake"]]
    for word in words:
        a, b = word
        if len(b) > len(a):
            # always string1 should be greater or equal to string2
            a, b = b, a
        print(one_edit_away(a, b))

