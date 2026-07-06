class Bank:
    """Bank details of a student"""

    bank_name = str
    account_number = str
    bank_branch = str

    def __init__(self, bank_name: str, account_number: str, bank_branch: str):
        self.bank_name: str = bank_name
        self.account_number: str = account_number
        self.bank_branch: str = bank_branch

    def __str__(self) -> str:
        masked_account = f"******{self.account_number[-4:]}" if len(self.account_number) >= 4 else self.account_number
        return f"{self.bank_name} ({self.bank_branch} Branch) - A/C: {masked_account}"

    def __repr__(self) -> str:
        return f"Bank(bank_name={self.bank_name!r}, account_number={self.account_number!r}, bank_branch={self.bank_branch!r})"