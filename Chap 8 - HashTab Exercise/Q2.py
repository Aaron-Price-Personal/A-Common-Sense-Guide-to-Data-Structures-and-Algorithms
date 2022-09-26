def findDuplicate(toSearch):
    dict1 = {}

    for each in toSearch:
        if each in dict1.keys():
            return each
            
        dict1[each] = True

    return None

def main():
    array1 = [item for item in input("Enter the list items : ").split()]
    print("Combined Array: ",findDuplicate(array1))

main()