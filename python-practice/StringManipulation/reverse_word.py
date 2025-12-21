def reverse_word(s):
    s = s.split()
    s = s[::-1]
    s = " ".join(s)
    return s

s = input("Enter your word: ")
print(reverse_word(s))