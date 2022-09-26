def find_x(toSearch):
    if toSearch[0] == "x":
        return 0
    return 1 + find_x(toSearch[1:])


print(find_x("abcdex"))