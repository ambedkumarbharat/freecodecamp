def string_compression(s):
    count = 1
    com_string = ''
    for c in s:
        if com_string == "":
            com_string += c 
        elif c == com_string[-1]:
            count += 1
        else:
            com_string += str(count) + c
            count = 1
    com_string += str(count)

    return com_string if len(com_string) < len(s) else s

print(string_compression(input("Enter a String: ")))