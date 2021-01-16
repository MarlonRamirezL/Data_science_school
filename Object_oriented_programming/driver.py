from account import Account

class driver(Account):
    email=str
    password= str

    def __init__(self,name,document,email,password):
        super().__init__(name,document)
        self.email=email
        self.password= password
        