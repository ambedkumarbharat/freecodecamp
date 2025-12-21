def palindrome_string_checker(s):
    s = s.lower().replace(" ","")
    return s == s[::-1] 

print(palindrome_string_checker(input("Enter your String: ")))
