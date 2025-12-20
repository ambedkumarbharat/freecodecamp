def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n <= 0:
        return 'Argument must be an integer greater than 0.'
    else:
        number = ""
        for i in range(1,n+1):
            number += " " + str(i)
        number.strip()
        return number