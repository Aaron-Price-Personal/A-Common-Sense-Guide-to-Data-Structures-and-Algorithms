'''
Function takes an implementation that can handle -ve values that
naive implementation could not
'''

def findGreatestNumber(tosearch):
    if len(tosearch) == 0:
        return None

    greatest_number_index = 0   
    for i in range(0,len(tosearch)-1):
        if tosearch[i+1] > tosearch[i]:
            greatest_number_index = i+1
    
    return tosearch[greatest_number_index]

print(findGreatestNumber([-3,-5,-6,-9,-1]))