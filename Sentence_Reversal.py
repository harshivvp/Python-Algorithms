#One-Line simple solutions:

def rev_word1(str):

    return " ".join(reversed(str.split()))

def rev_word2(str):

    return " ".join(str.split()[::-1])

print(rev_word1("Hello string prepare to be reversed"))
print(rev_word2("Hello string prepare to be reversed"))

def rev_word_long(str):

    words = []
    length = len(str)
    spaces = [' ']

    i = 0 # Index tracker

    while i < length:

        if str[i] not in spaces:

            word_start = i

            while i < length and str[i] not in spaces:

                i += 1

            words.append(str[word_start:i])

        i += 1

    return " ".join(reversed(words))

print(rev_word_long("   Hello John sample    "))

