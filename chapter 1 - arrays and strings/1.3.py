def urlify_inbuilf(url):
    # doesn't uses the length of string
    return url.strip().replace(" ", "%20")


def urlify(url, str_length):
    result = []
    for i in range(str_length):
        char = "%20" if url[i] == " " else url[i]
        result.append(char)
    return "".join(result)


if __name__ == "__main__":
    str = "Mr John Smith    "
    result = urlify(str, 13)
    print(result)
    print(urlify_inbuilf(str))

