def total_chars(array_to_count):
    if len(array_to_count) == 0:
        return 0
    return len(array_to_count[0]) + total_chars(array_to_count[1:])


print(total_chars(["ab","c","def","ghij"]))