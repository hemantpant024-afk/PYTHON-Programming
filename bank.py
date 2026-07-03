class Customer: #class customer
    def get_customer(self): #puruose: takes the coustomers name and account number. 
        self.name = input("Enter Customer Name: ") #def for function methord.  
        self.acc_no = input("Enter Account Number: ")


class Bank:
    def get_balance(self):
        self.balance = int(input("Enter Balance: "))

    def display(self, customer):
        print("\n----- Bank Details -----")
        print("Customer Name:", customer.name)
        print("Account Number:", customer.acc_no)
        print("Balance:", self.balance)


# Create Objects
c1 = Customer()
b1 = Bank()

# Call Functions
c1.get_customer()
b1.get_balance()

# Display Details
b1.display(c1)
