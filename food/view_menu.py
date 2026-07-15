def view_menu():
    print("FOOD MENU")
    for key, value in menu.items():
        print(key, ".", value[0], " - Rs.", value[1])