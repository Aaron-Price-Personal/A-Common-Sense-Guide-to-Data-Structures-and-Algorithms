def shortest_path(rows,cols):
    if rows == 1 and cols == 1:
        return 0
    elif rows <= cols and rows > 1:
        return 1 + shortest_path(rows-1,cols)
    else:
        return 1 + shortest_path(rows,cols-1)


def unique_paths(rows,cols):
    if rows == 1 or cols == 1:
        return 1
    return unique_paths(rows-1,cols) + unique_paths(rows,cols-1)

print(unique_paths(3,7))