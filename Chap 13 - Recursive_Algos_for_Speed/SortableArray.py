class SortableArray():
    def __init__(self,data):
        self.data = data
    
    def partition(self, left_pointer, right_pointer):
        # Choose righ most elem as pivot
        pivot_index = right_pointer

        pivot = self.data[pivot_index]

        right_pointer -= 1

        while True:
            # Move left pointer to right as long as it points to calue less than pivot
            while self.data[left_pointer] < pivot:
                left_pointer += 1
            
            # Move right pointer to left as long as it points to value greater than pivot
            while self.data[right_pointer] > pivot:
                right_pointer -= 1
            
            # Now check whether left pointer has reached or gone beyond right.
            # If it has break loop so we can swap the pivot later
            if left_pointer >= right_pointer:
                break

            # If left pointer is stll to left of the right, swap values
            else:
                self.data[left_pointer], self.data[right_pointer] = self.data[right_pointer], self.data[left_pointer]

                # Move left pointer over to the rigt, gearing up for next round of left and right pointer movements
                left_pointer += 1
        
        # Final step swap values of lef tpointer with pivot
        self.data[left_pointer], self.data[pivot_index] = self.data[pivot_index], self.data[left_pointer]

        # Return left_pointer for sake of quicksort method
        return left_pointer
    
    def quicksort(self,left_index, right_index):
        # Base case
        if right_index - left_index <= 0:
            return
        
        # Partition the range of elements and grab the index of the pivot:
        pivot_index = self.partition(left_index,right_index)

        # Recursively call this quicksort ethod on whathever is left of the pivot
        self.quicksort(left_index, pivot_index-1)

        # Recusively call this quicksort method on whatever of right of pivot
        self.quicksort(pivot_index+1, right_index)
    
    def quickselect(self, kth_lowest_val, left_index, right_index):
        # Base case
        if right_index - left_index <= 0:
            return self.data[left_index]
        
        # Partition the array
        pivot_index = self.partition(left_index,right_index)

        # If left of pivot
        if kth_lowest_val < pivot_index:
            self.quickselect(kth_lowest_val, left_index,pivot_index-1)
        # if right of pivot
        elif kth_lowest_val > pivot_index:
            self.quickselect(kth_lowest_val,pivot_index+1, right_index)
        # Pivot must equal kth_lowest val therefor return val we looking for
        else:
            return self.data[pivot_index]
