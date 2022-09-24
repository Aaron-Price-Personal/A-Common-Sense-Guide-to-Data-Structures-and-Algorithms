def count_even(array_to_count):
    if len(array_to_count) == 0:
        return 0

    if (array_to_count[0] % 2) == 0:
        return 1 + count_even(array_to_count[1:])
    else:
        return count_even(array_to_count[1:])
    
print(count_even([1,2,3,4,5,5,6,7,6]))