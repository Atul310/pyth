class ATM:
    def __init__(self):
        self.pin =""
        self.balance =0
        self.menu()
        
    def menu(self):
       user_input = input("""
              Hi can  I help you ?
              1. press 1 to create pin 
              2. press 2 to chage the pin 
              3. check balance at 3
              4. 4 to withdraw 
              5 . 5 to exit 
              """)
       if user_input =="1":
           self.create_pin()
       elif user_input == "2":
           self.chage_pin()
       elif user_input=="3":
           self.check_balance()
       elif user_input=="4":
           self.check_balance()    
    def create_pin(self):
        Usr_pn = input("enter pin")
        self.pin =Usr_pn
        usr_bal = input("enter balanec")
        self.balance= usr_bal
        print("created pin")
        self.menu()
    def chage_pin(self):
        user_pin = input("enter the old pin ")
        if user_pin == self.pin:
            new_pin = input("enter new pin")
            self.pin = new_pin
            self.menu()
            
            
        else:
          print("incorrect pin try again !!!")
          self.menu()
    def check_balance(self):
        usr_pin =input("input pin")
        if self.pin == usr_pin:
            print(" your balance is :",self.balance)
        else:
            print("your pin is incorrect")
    def Withdraw(self):
        user_iinp =input("first enter pin")
        if user_iinp == self.pin:
            #print("enter the amount to withdraw")
            amount = int(input("enter ampunt"))
            if amount <= self.balance:
             slef.balance= balance-amount
             print("withdrawn successfull")
            else:
                print("try agatin")
            
            
        
        else:
            print("please correct your pin and try again")
        self.menu()
    
            
        
        
        
        
a = ATM()