initial_list = [1, 2, 3, 2, 1]
copy_list = initial_list.copy()
copy_list.reverse()

if initial_list == copy_list:
    print("палиндром")
else:
    print("не палиндромом")