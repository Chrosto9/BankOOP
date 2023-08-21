class Bank:
    is_national: bool = False

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Bank {self.name}"
    
    @classmethod
    def changeStatus(cls, changeStatus):
        cls.is_national = changeStatus


amber = Bank("Amber Gold")
print(amber)
amber.changeStatus(True)
print (amber.is_national)