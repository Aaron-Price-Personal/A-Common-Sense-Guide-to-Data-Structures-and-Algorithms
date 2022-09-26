import time

def SelectionSort(toSort):
    for i in range(1,len(toSort)-1):
        lowest_number_index = i
        for j in range(i+1,len(toSort)):
            if toSort[j] < toSort[lowest_number_index]:
                lowest_number_index = j
        
        if (lowest_number_index != i):
            temp = toSort[i]
            toSort[i] = toSort[lowest_number_index]
            toSort[lowest_number_index] = temp
    return toSort

def time_difference(start,end):
    return end - start

def main():
    array_toSort = [int(item) for item in input("Enter the list items : ").split()]
    start_time = time.time()
    print("Sorted Array: ",SelectionSort(array_toSort))
    end_time = time.time()
    print("The time taken to execute: {}".format(time_difference(start_time,end_time)))

main()