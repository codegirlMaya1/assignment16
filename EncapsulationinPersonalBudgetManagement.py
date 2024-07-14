
class BudgetCategory:
    def __init__(self):
        self.balance=0
        self.food_category=-100
        self.fun_category=-100
        self.display()
        print("Hello!!! Welcome to your online budget assistant. How can we help you?")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Please enter the total amount to be withdrawn for food today: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You are still within budget. You Withdrew:", amount)
            print( "Please make another selection. Enter 200 to deposit the accepted max limit for today. Enter 50 to withdraw money allotted for some fun activities today! Enter 3 to exit the system....")
            amount = float(input("Please enter your selection:  ") )
            if amount ==100:
                self.balance += amount
                print("\n Amount Deposited:",amount)
            elif amount==50:
                if self.balance>=amount:
                    self.balance-=amount
                    print("\n Amount Deposited:",amount)
                    print("\n You are still within budget. You Withdrew:", amount,)
            
            elif amount==3:
                def display(self):
                    display(self)==True
                    print ("Thanks for visiting the online budget assistant. Now exiting the system....")
        else:
            print("\n Insufficient balance  ")
            

    def food_category(self,food):
        amount = float(input("Enter amount to be Withdrawn: "))
        food== -100
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
            print( "Your on a budget. Please enter a different amount to purchase available entrees")
            
    def fun_category(self,fun):
        amount = float(input(" Please enter the amount you are withdrawing for food today....: "))
        fun== -100
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
            print( "Your on a budget. Please enter a different amount to withdraw for liesure activities today....")
    def display(self):
        print("\nAvailable Spending Balance = ",self.balance,"Unavailable Balance is securely in your savings account")
        
 
# Driver code
  
# creating an object of class
s = BudgetCategory()

   
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()



