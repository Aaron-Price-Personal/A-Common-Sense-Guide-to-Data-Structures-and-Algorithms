def print_array(toPrint):
    for value in toPrint:
        if isinstance(value,list):
            print_array(value)
        else:
            print(value)



array_to_print = [1,2,3,[4,5,6],7,[8,[9,10,11,[12,13,14]]],[15,16,17,18,[19,[20,21]]],22]

print_array(array_to_print)