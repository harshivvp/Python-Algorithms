def compress(s):

    r = "" # returns the string's compressed value
    l = len(s) # Length of the uncompressed string

    if l == 0:
        return "Enter String!"

    if l == 1:
        return s + "1" #Will just return the string passed (s) and add 1 behind it since len is 1

    cnt = 1 #counter which checks the amount of times letter is found
    i = 1 #index marker

    while i < l:
        if s[i] == s[i-1]: #Check if current index letter of string is the same as the last one.
            cnt += 1 # if so then add one to counter
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        i += 1


    r = r + s[i-1] + str(cnt)
    return r

print(compress("ASD"))