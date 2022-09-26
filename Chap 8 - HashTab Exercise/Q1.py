import time

def intersetion(array1,array2):
    dict1 = {}
    combined = []

    for each in array1:
        dict1[each] = True
    
    for each in array2:
        try: 
            if dict1[each]:
                combined.append(each)
        except:
            "Nothing"

    return combined

def time_difference(start,end):
    return end - start

def main():
    array1 = [int(item) for item in input("Enter the list items : ").split()]
    array2 = [int(item) for item in input("Enter the list items : ").split()]
    start_time = time.time()
    print("Combined Array: ",intersetion(array1,array2))
    end_time = time.time()
    print("The time taken to execute: {}".format(time_difference(start_time,end_time)))

main()