def register():
    username = input("Enter New Username : ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter Password : ")
    users[username] = password
    print("Registration Successful.")