
def print_multiplication_table():
    max_number = 10
    for row in range(1, max_number + 1):
        for column in range(1, max_number + 1):
            print(row * column, end='\t')
        print()


print_multiplication_table()
