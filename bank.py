# Bank 
class Bank:
    """Bank details of a student"""

    bank_name = str
    account_number = str
    bank_branch = str

    def __init__(self, bank_name: str, account_number: str, bank_branch: str):
        self.self.bank_name: str = bank_name # type: ignore
        self.self.account_number: str = account_number # type: ignore
        self.self.bank_branch: str = bank_branch # type: ignore

    def display(self):
        print("bank_name:", self.bank_name)
        print("account_number:", self.account_number)
        print("bank_branch:", self.bank_branch)