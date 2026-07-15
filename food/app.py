users = {
    "vamsi": "1234",
    "rahul": "5678",
    "ashok": "91011"
    }
menu = {
    1: ("Pizza", 250),
    2: ("Burger", 120),
    3: ("Biryani", 200),
    4: ("Fried Rice", 180),
    5: ("Cool Drink", 50)
}
cart = []
logged_user = None

def register():
    username = input("Enter New Username : ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter Password : ")
    users[username] = password
    print("Registration Successful.")
def login():
    global logged_user
    username = input("Username : ")
    password = input("Password : ")
    if username in users and users[username] == password:
        logged_user = username
        print("Login Successful")
    else:
        print("Invalid Username or Password")
def view_menu():
    print("FOOD MENU")
    for key, value in menu.items():
        print(key, ".", value[0], " - Rs.", value[1])
def add_to_cart():
    view_menu()
    item = int(input("Enter Item Number : "))
    if item in menu:
        cart.append(menu[item])
        print(menu[item][0], "Added Successfully")
    else:
        print("Invalid Item")
def view_cart():
    if len(cart) == 0:
        print("Cart is Empty")
        return
    total = 0
    print("YOUR CART")
    for item in cart:
        print(item[0], "- Rs.", item[1])
        total += item[1]
    print("Total =", total)
def place_order():
    if len(cart) == 0:
        print("Cart is Empty")
        return
    total = 0
    for item in cart:
        total += item[1]
    print("Order Placed Successfully")
    print("Total Bill = Rs.", total)
    cart.clear()
def cancel_order():
    if len(cart) == 0:
        print("Cart Already Empty")
    else:
        cart.clear()
        print("Order Cancelled")
def user_menu():
    while True:
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Place Order")
        print("5. Cancel Order")
        print("6. Logout")
        choice = input("Enter Choice : ")
        if choice == "1":
            view_menu()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_cart()
        elif choice == "4":
            place_order()
        elif choice == "5":
            cancel_order()
        elif choice == "6":
            print("Logged Out Successfully")
            break
        else:
            print("Invalid Choice")
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter Choice : ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
        if logged_user is not None:
            user_menu()
    elif choice == "3":
        print("Thank You")
        break
    else:
        print("Invalid Choice")