import time


def BubbleSort(tosort):
    unsorted_util_index = len(tosort) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_util_index):
            if tosort[i] > tosort [i+1]:
                tosort[i], tosort[i+1] = tosort[i+1], tosort[i]
                sorted = False
        unsorted_util_index -= 1
    return tosort

def time_difference(start,end):
    return end - start

def main():
    array_toSort = [int(item) for item in input("Enter the list items : ").split()]
    start_time = time.time()
    print("Sorted Array: ",BubbleSort(array_toSort))
    end_time = time.time()
    print("The time taken to execute: {}".format(time_difference(start_time,end_time)))


main()