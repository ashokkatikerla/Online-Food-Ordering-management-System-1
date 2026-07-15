def login():
    global logged_user
    username = input("Username : ")
    password = input("Password : ")
    if username in users and users[username] == password:
        logged_user = username
        print("Login Successful")
    else:
        print("Invalid Username or Password")