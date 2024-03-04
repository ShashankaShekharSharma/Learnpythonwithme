def get_matrix(rows, columns):
    matrix = []
    print(f"Enter {rows} rows with {columns} elements each: ")
    for _ in range(rows):
        row = list(map(int,input().split()))
        if len(rows) != columns:
            print(f"Invalid input. Enter exactly {columns} elements for each row.")
            return get_matrix(rows, columns)