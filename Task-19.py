
def get_user_input():
    user_array = []
    while len(user_array) < 5:
        user_array.append(int(input(f"Введите число №{len(user_array) + 1} ")))
    print(user_array)


get_user_input()
