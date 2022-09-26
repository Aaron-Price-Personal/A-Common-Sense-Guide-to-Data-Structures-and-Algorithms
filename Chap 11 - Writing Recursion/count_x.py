def count_x(stringToCount):
    if len(stringToCount) == 0:
        return 0
    
    if stringToCount[0] == "x":
        return 1 + count_x(stringToCount[1:])
    else:
        return 0 + count_x(stringToCount[1:]) 

print(count_x("axbxcxd"))