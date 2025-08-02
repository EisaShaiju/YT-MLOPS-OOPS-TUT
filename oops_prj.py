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
            self.signup()
        elif user_input =="2":
            self.signin()
        elif user_input =="3":
            self.my_post()
        elif user_input=="4":
            self.send_msg()
        else:
            exit()

    def signup(self):
        email=input("Enter your email here -> ")
        pwd=input("setup your password here -> ")
        self.username=email
        self.password=pwd
        print("You have successfully signed up")
        print("\n")
        self.menu()

    def signin(self):
        if self.username==''and self.password=='':
            print("Please signup by pressing 1 in the main menu")
        else:
            uname=input("Please enter your username here->")
            pwd=input("Please enter your password here->")
            if(self.username==uname and self.password==pwd):
                print("You have signed in successfully")
                self.loggedin=True
            else :
                print("Please input correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("What is on your mind today ??")
            print(f"Following content has been posted ->{txt}")
        else:
            print("You need to signin first")
        print("\n")
        self.menu()
    
    def send_msg(self):
        if self.loggedin==True:
            txt=input("Enter your message here ->")
            frnd=input("Whom to send the message to ->")
            print(f"The message has been sent to {frnd}")
        else:
            print("You need to signin first")
        print("\n")
        self.menu()


obj=chatbook()

