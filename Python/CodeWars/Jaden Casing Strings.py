def to_jaden_case(string):
    return " ".join([x[0].upper() + x[1:] for x in string.split()])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))