def num_of_paths(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    
    return num_of_paths(n-1) + num_of_paths(n-2) + num_of_paths(n-3)


num_of_stairs = 4
print(num_of_paths(num_of_stairs))