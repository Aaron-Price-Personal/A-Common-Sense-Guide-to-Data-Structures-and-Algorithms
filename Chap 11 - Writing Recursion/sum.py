def sumArray(toSum):
    if len(toSum) == 1:
        return toSum[0]

    return toSum[0] + sumArray(toSum[1:])

print(sumArray([1,2,3,4,5]))