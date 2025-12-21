def count_substring_character(s):
    char = ""
    count = 0
    for c in s:
        if c not in char:
            count += 1
            char += c
    return count

print(count_substring_character(input("Enter your String: ")))