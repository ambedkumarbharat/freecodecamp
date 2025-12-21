def count_character(s):

    s = s.replace(" ",'').lower()
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
    
        else:
            char_count[c] = 1
    return char_count

print(count_character(input("Enter your sentence: ")))