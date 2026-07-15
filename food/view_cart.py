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