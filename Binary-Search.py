def BinarySearch(toSearch,value):
    lower = 0
    upper = len(toSearch) -1

    while lower <= upper:
        midpoint = getMidpoint(upper,lower)
        midpoint_value = toSearch[midpoint]

        if midpoint_value == value:
            return True
        elif midpoint_value > value:
            upper = midpoint - 1
        elif midpoint_value < value:
            lower = midpoint + 1
    
    return False

def getMidpoint(upper,lower):
    return (upper + lower) // 2

def __main__():
    array_toSearch = [int(item) for item in input("Enter the list items : ").split()]
    value = int(input("Please supply a value to search within array: "))
    print("The answer to is the value {} located in array is: {}".format(value,BinarySearch(array_toSearch,value)))

__main__()