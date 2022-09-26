import time

def InsertionSort(toSort):
    for index in range(1,len(toSort)):
        temp_value = toSort[index]
        position = index - 1

        while position >= 0:
            if toSort[position] > temp_value:
                toSort[position+1] = toSort[position]
                position -= 1
            else:
                break
        
        toSort[position+1] = temp_value
    
    return toSort

def time_difference(start,end):
    return end - start

def main():
    array_toSort = [int(item) for item in input("Enter the list items : ").split()]
    start_time = time.time()
    print("Sorted Array: ",InsertionSort(array_toSort))
    end_time = time.time()
    print("The time taken to execute: {}".format(time_difference(start_time,end_time)))

main()