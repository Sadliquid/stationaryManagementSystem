# Name: Joshua Long Yu Xuan
# Student Admin Number: 230627W
# Tutorial Group: IT2153-01

prodList = []

class Stationary:
    def __init__(self, productID, productName, category, brand, supplierYear):
        self.productID = productID
        self.productName = productName
        self.category = category
        self.brand = brand
        self.supplierYear = supplierYear

    def get_productID(self):
        return self.productID
    
    def get_productName(self):
        return self.productName
    
    def get_category(self):
        return self.category
    
    def get_brand(self):
        return self.brand
    
    def get_supplierYear(self):
        return self.supplierYear



def addStationary():
    global prodList
    while True:
        try:
            newProductID = str(input("Enter Product ID: "))
            newProductName = str(input("Enter Product Name: "))
            newProductCategory = str(input("Enter Product Category: "))
            newProductBrand = str(input("Enter Brand: "))
            newProductSupplierYear = int(input("Please enter the year this supplier started supplying this product: "))
            break
        except ValueError:
            print("Invalid Inputs. Please try again.")
    newProduct = Stationary(newProductID, newProductName, newProductCategory, newProductBrand, newProductSupplierYear)
    prodList.append(newProduct)
    print("Product added successfully!\n")
    

def displayStationary():
    global prodList
    if len(prodList) == 0:
        print("There are currently no products in the system!")
    else:
        print("---------------------Products List---------------------")
        for i in range(len(prodList)):
            print(f"Product ID: {prodList[i].get_productID()}")
            print(f"Product Name: {prodList[i].get_productName()}")
            print(f"Product Category: {prodList[i].get_category()}")
            print(f"Brand: {prodList[i].get_brand()}")
            print(f"Supplier Year: {prodList[i].get_supplierYear()}")
            print("-----------------------------------------------")

def bubbleSortStationary():
    global prodList
    if len(prodList) == 0:
        print("No stationary to sort!")
    else:
        prodListLength = len(prodList)
        for i in range(prodListLength - 1):
            for j in range(0, prodListLength - i - 1):
                if prodList[j].get_category() > prodList[j+1].get_category():
                    prodList[j], prodList[j+1] = prodList[j+1], prodList[j]

            print(f"Pass {i+1}:")
            print("-----------------------------------------------")
            for k in range(len(prodList)):
                print(f"Product_ID: {prodList[k].get_productID()}")
            print("-----------------------------------------------")
        
        print("---------------Sorted Stationary List---------------")
        for product in range(len(prodList)):
            print(f"Product ID: {prodList[product].get_productID()}")
            print(f"Product Name: {prodList[product].get_productName()}")
            print(f"Product Category: {prodList[product].get_category()}")
            print(f"Brand: {prodList[product].get_brand()}")
            print(f"Supplier Year: {prodList[product].get_supplierYear()}")
            print("-----------------------------------------------")
                

def insertionSortStationary():
    global prodList
    if len(prodList) == 0:
        print("No stationary to sort!")
    else:
        prodListLength = len(prodList)
        for i in range(1, prodListLength):
            key = prodList[i]
            j = i - 1
            while j >= 0 and key.get_brand() > prodList[j].get_brand():
                prodList[j + 1] = prodList[j]
                j -= 1
            prodList[j + 1] = key
            
            print(f"Pass {i}:")
            print("-----------------------------------------------")
            for k in range(len(prodList)):
                print(f"{prodList[k].get_productID()}")
            print("-----------------------------------------------")

        print("---------------Sorted Stationary List---------------")
        for product in range(len(prodList)):
            print(f"Product ID: {prodList[product].get_productID()}")
            print(f"Product Name: {prodList[product].get_productName()}")
            print(f"Product Category: {prodList[product].get_category()}")
            print(f"Brand: {prodList[product].get_brand()}")
            print(f"Supplier Year: {prodList[product].get_supplierYear()}")
            print("-----------------------------------------------")

def populateData(): # To populate data and for testing purposes
    global prodList
    prodList = []
    newStudA = Stationary("PD1020", "Pastel Art Paper", "Paper", "Faber-Castell", 2021)
    prodList.append(newStudA)
    newStudA = Stationary("PD1025", "Mars Lumograph Drawing Pencils", "Pencils", "Staedtler", 2022)
    prodList.append(newStudA)
    newStudA = Stationary("PD1015", "Water color Pencils", "Pencils", "Faber-Castell", 2011)
    prodList.append(newStudA)
    newStudA = Stationary("PD1050", "Noris 320 fiber tip pen", "Pens", "Staedtler", 2021)
    prodList.append(newStudA)
    newStudA = Stationary("PD1001", "Copier Paper (A4) 70GSM", "Paper", "PAPERONE", 2021)
    prodList.append(newStudA)
    newStudA = Stationary("PD1033", "Scientific Calculator FX-97SG X", "Calculator", "CASIO", 2022)
    prodList.append(newStudA)
    newStudA = Stationary("PD1005", "Pop Bazic File Separator Clear", "Office Supplies", "Popular", 2000)
    prodList.append(newStudA)
    print("Data populated!\n")
    return prodList
                

def menu():
    global prodList
    while True:
        print()
        print("------------------Stationary Management System------------------")
        print("1. Add a new Stationary.")
        print("2. Display all Stationary.")
        print("3. Sort Stationary via Bubble Sort on Category.")
        print("4. Sort Stationary via Insertion Sort on Brand.")
        print("5. Populate data.")
        print("6. Exit program.")

        try:
            choice = int(input("Please select one: "))
            if choice == 1:
                addStationary()
            elif choice == 2:
                displayStationary()
            elif choice == 3:
                bubbleSortStationary()
            elif choice == 4:
                insertionSortStationary()
            elif choice == 5:
                prodList = populateData()
            elif choice == 6:
                print("Good bye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number ranging from 1-6.")


menu()