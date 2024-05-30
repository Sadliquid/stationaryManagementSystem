# Name: Joshua Long Yu Xuan
# Student Admin Number: 230627W
# Tutorial Group: IT2153-01

class Stationary:
    def __init__(self, productID, productName, category, brand, supplierYear):
        self.productID = productID
        self.productName = productName
        self.category = category
        self.brand = brand
        self.supplierYear = supplierYear

    def get_productID(self):
        return self.productID
    
    def set_productID(self, productID):
        self.productID = productID
    
    def get_productName(self):
        return self.productName
    
    def set_productName(self, productName):
        self.productName = productName
    
    def get_category(self):
        return self.category
    
    def set_category(self, category):
        self.category = category
    
    def get_brand(self):
        return self.brand
    
    def set_brand(self, brand):
        self.brand = brand
    
    def get_supplierYear(self):
        return self.supplierYear
    
    def set_supplierYear(self, supplierYear):
        self.supplierYear = supplierYear