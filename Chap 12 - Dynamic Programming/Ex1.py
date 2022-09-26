def add_until_100(array_to_add):
    if len(array_to_add) == 0:
        return 0
    
    sum_checker = add_until_100(array_to_add[1:])

    if array_to_add[0] + sum_checker > 100:
        return sum_checker
    else:
        return array_to_add[0] + sum_checker
    
print(add_until_100([20,23,25,18,20,75]))