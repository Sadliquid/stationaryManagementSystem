# Name: Joshua Long Yu Xuan
# Student Admin Number: 230627W
# Tutorial Group: IT2153-01

class Stationary:
    def __init__(self, Prod_id, ProdName, category, brand, Supplier_since, Stock):
        self.Prod_id = Prod_id
        self.ProdName = ProdName
        self.category = category
        self.brand = brand
        self.Supplier_since = Supplier_since
        self.Stock = Stock

    def get_Prod_id(self):
        return self.Prod_id
    
    def set_Prod_id(self, Prod_id):
        self.Prod_id = Prod_id
    
    def get_ProdName(self):
        return self.ProdName
    
    def set_ProdName(self, ProdName):
        self.ProdName = ProdName
    
    def get_category(self):
        return self.category
    
    def set_category(self, category):
        self.category = category
    
    def get_brand(self):
        return self.brand
    
    def set_brand(self, brand):
        self.brand = brand
    
    def get_Supplier_since(self):
        return self.Supplier_since
    
    def set_Supplier_since(self, Supplier_since):
        self.Supplier_since = Supplier_since

    def get_Stock(self):
        return self.Stock
    
    def set_Stock(self, Stock):
        self.Stock = Stock