from payment import Payment

class card(Payment):
    numbercard= str
    datecard= str
    cvv= str

    def __init__(self,numbercard, datecard, cvv):
        self.numbercard= numbercard
        self.datecard = datecard
        self.cvv= cvv