def findMissingNumber(tosearch):
    tosearch.sort()

    for i in range(0,len(tosearch)):
        if tosearch[i] != i:
            return i
    
    return None

toSearch = [0,1,2,7,6,8,5,4]
print(findMissingNumber(toSearch))