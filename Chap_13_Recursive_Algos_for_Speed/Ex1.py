from SortableArray import SortableArray

def largest_product_3(data):
    sortableArray = SortableArray(data)
    sortableArray.quicksort(0,len(data)-1)
    sorted_array = sortableArray.data

    product = 1

    for each in sorted_array[-3:]:
        product *= each
    
    return product

data = [0,5,3,1,10]
print(largest_product_3(data))
