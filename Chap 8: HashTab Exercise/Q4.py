def nonDuplicate(toSearch):
    char_occurunces = {}

    for each in toSearch:
        if each in char_occurunces.keys():
            char_occurunces[each] += 1
        else:
            char_occurunces[each] = 1

    return list(filter(lambda elem: elem[1] == 1, char_occurunces.items())) #char_single_occurunce

def main():
    user_input = input("Enter the list items : ")
    print("Combined Array: ",nonDuplicate(user_input))

main()