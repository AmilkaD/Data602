class BankAccount:
    def __init__(self,bankname,firstname,lastname,balance = 0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
        
    def deposit(self):
        while True:
            try:
                amount = float(input("Enter the amount you wish to Deposit: $"))
                if amount > 0:
                    self.balance += amount
                    print(amount,'Has been deposited in your account, your current balance is: $', self.balance)
                    return
                else:
                    print("Cannot deposit a negative ammount")  
            except ValueError:
                print("Invalid Input. Please try again")
                
    def withdraw(self):
        while True:
            try:
                amount = float(input("Enter amount you wish to withdraw: $"))
                if amount > 0:
                   if self.balance >= amount:
                      self.balance -= amount
                      print(amount, 'has been withdrawn from your account, your current balance is: $',self.balance)
                      return self.balance
                   else:
                       print('error: cannot withdraw more than available balance of $', self.balance)
                else: 
                  print("Cannot withdraw negative ammount")
            except ValueError:
                print("Invalid Input. Please try again")

    
    def __str__(self):
        print('Account Details:', 'Bank:', self.bankname,'Customer Name:', self.firstname, self.lastname, 'Account Balance: $', self.balance) 
    
    def menu(self):
        print("Welcome to Amilka Bank, What would you like to do today?")
        print("1. Deposit Funds")
        print("2. Withdraw funds")
        print("3. Account details")
        print("Exit")

    def ATM(self):
        while True:
            self.menu()
            choice = input("Enter Choice")
            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
               self.__str__()
            elif choice == '4':
                print("Thank you for using Amilka Bank. Come Again!")
                
            else:
                print("The Choice you entered is invalid. Please try Again
                
if __name__ == "__main__":
    ATM = BankAccount('Amilka Bank','Amilka','Diaz')
    ATM.ATM()

class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def render(self):
        for _ in range(self.length):
            print("*" * self.width)
            
    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.length)
        
    def invert(self):
        self.width, self.length = self.length, self.width
    
    def double(self):
        self.width  *= 2
        self.length *= 2
        
    def __eq__(self, other):
        if not isinstance(other, Box):
            return False
        return (self.width == other.width and self.length == other.length)

    def print_dim(self):
        print('The length of this box is',self.length)
        print('The width of this box is',self.width)

    def combine(self, other):
        self.width += other.width  
        self.length += other.length
        
    def get_hypot(self):
        hypotwidth = (self.width ** 2)
        hypotlength = (self.length ** 2)
        sqrroot = (hypotwidth + hypotlength) ** 0.5
        return sqrroot
         

MyBox = Box(4,5)
MyBox1 = Box(5,10)
MyBox2 = Box(3,4)
MyBox3 = Box(5,10)
MyBox.double()
MyBox.render()
print(MyBox)
print(MyBox1.__eq__(MyBox2))
print(MyBox1 == MyBox3)
MyBox.render()
MyBox.print_dim()
MyBox1.render()
MyBox1.print_dim()
MyBox2.render()
MyBox2.print_dim()
MyBox3.render()
MyBox3.print_dim()
MyBox1.combine(MyBox3)
MyBox2.double()
MyBox1.combine(MyBox2)




