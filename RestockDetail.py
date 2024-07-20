# Name: Joshua Long Yu Xuan
# Student Admin Number: 230627W
# Tutorial Group: IT2153-01

class RestockDetail:
    def __init__(self, Prod_id, quantity):
        self.Prod_id = Prod_id
        self.quantity = quantity

    def get_Prod_id(self):
        return self.Prod_id
    
    def set_Prod_id(self, Prod_id):
        self.Prod_id = Prod_id

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity