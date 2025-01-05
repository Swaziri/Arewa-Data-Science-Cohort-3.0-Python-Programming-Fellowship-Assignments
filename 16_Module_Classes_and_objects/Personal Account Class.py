class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # List of tuples: [(description, amount)]
        self.expenses = []  # List of tuples: [(description, amount)]

    def total_income(self):
        return sum(amount for _, amount in self.incomes)

    def total_expense(self):
        return sum(amount for _, amount in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def add_income(self, description, amount):
        self.incomes.append((description, amount))

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def account_info(self):
        return {
            "Firstname": self.firstname,
            "Lastname": self.lastname,
            "Total Income": self.total_income(),
            "Total Expense": self.total_expense(),
            "Account Balance": self.account_balance(),
        }

# Example usage
person = PersonAccount("Muhammad", "Waziri")
person.add_income("Salary", 5000)
person.add_income("Freelancing", 2000)
person.add_expense("Rent", 1500)
person.add_expense("Groceries", 500)

print("Total Income:", person.total_income())
print("Total Expense:", person.total_expense())
print("Account Balance:", person.account_balance())
print("Account Info:", person.account_info())
