from payment import Payment

class paypal(Payment):
    email=str
    password= str

    def __init__(self,email, password):
        self.email=email
        self.password=password
        