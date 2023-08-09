def duplicate_encode(word):
    return "".join([")" if list(word.lower()).count(x.lower()) > 1 else "(" for x in list(word)])

print(duplicate_encode("recede"))