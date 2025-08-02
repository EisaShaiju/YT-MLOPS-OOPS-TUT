class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()


    def menu(self):
        user_input=input("""Welcome to Chatbook, How would you like to proceed ?
                        1. press to signup
                        2. press to signin
                        3. press to message a friend
                        4. press to exit""")
        if user_input =="1":
            pass
        elif user_input =="2":
            pass
        elif user_input =="3":
            pass
        else:
            exit()

obj=chatbook()