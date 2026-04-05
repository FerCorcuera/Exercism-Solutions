def reverse(text):
    new = list(text)
    rev = ''
    for x in reversed(new):
        rev = rev + x

    return rev
