def golomb(n,memo={}):
    if n == 1:
        return 1
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = 1 + golomb(n-golomb(golomb(n-1,memo),memo),memo)