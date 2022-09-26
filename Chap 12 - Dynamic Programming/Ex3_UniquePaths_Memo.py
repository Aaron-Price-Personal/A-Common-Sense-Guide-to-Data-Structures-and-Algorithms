def unique_paths(rows,cols,memo={}):
    if rows == 1 or cols == 1:
        return 1
    if not((rows,cols) in memo.keys()):
        memo[(rows,cols)] = unique_paths(rows-1,cols,memo) + unique_paths(rows,cols-1,memo)
    return memo[(rows,cols)]
        
    

print(unique_paths(3,7))