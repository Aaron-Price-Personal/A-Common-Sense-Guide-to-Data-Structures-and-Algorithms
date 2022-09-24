def reverseString(toReverse):
    if len(toReverse) == 1:
        return toReverse
    
    return reverseString(toReverse[1:]) + toReverse[0]

string_to_reverse = "abcde"
print(reverseString(string_to_reverse))