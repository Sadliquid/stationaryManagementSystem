# Name: Joshua Long Yu Xuan
# Student Admin Number: 230627W
# Tutorial Group: IT2153-01

from Stationary import Stationary

prodDict = {} # global dictionary


def addStationary():
    global prodDict
    productKeysList = list(prodDict.keys())
    while True:
        newProductID = str(input("Enter Product ID: "))
        if newProductID in productKeysList:
            print()
            print("Product ID already exists. Please enter a unique Product ID.")
            print()
        else:
            break
    newProductName = str(input("Enter Product Name: "))
    newProductCategory = str(input("Enter Product Category: "))
    newProductBrand = str(input("Enter Brand: "))

    while True:
        newProductSupplier_since = input("Please enter the year this supplier started supplying this product: ")
        try:
            newProductSupplier_since = int(newProductSupplier_since)
            if len(str(newProductSupplier_since)) == 4 and newProductSupplier_since > 0:
                break
            else:
                print()
                print("Please enter a valid positive year (YYYY).")
                print()
        except ValueError:
            print()
            print("Only numbers are allowed. Please enter a valid year (YYYY).")
            print()

    while True:
        newProductStock = input("Please enter the stock quantity: ")
        try:
            newProductStock = int(newProductStock)
            if newProductStock > 0:
                break
            else:
                print()
                print("Product stock must be more than 0.")
                print()
        except ValueError:
            print()
            print("Only numbers are allowed. Please enter a valid number.")
            print()

    newProduct = Stationary(newProductID, newProductName, newProductCategory, newProductBrand, newProductSupplier_since, newProductStock)
    prodDict[newProduct.get_Prod_id()] = newProduct # using newProductID as the {PK}
    print()
    print("Product added successfully!")
    

def displayStationary():
    global prodDict
    if len(prodDict) == 0:
        print()
        print("There are currently no products in the system!")
    else:
        print()
        print("---------------------Products List---------------------")
        for stationary in prodDict.values():
            print(f"Product ID: {stationary.get_Prod_id()}")
            print(f"Product Name: {stationary.get_ProdName()}")
            print(f"Product Category: {stationary.get_category()}")
            print(f"Brand: {stationary.get_brand()}")
            print(f"Supplier Year: {stationary.get_Supplier_since()}")
            print(f"Stock: {stationary.get_Stock()}")
            print("-----------------------------------------------")

def bubbleSortStationary():
    global prodDict
    tempProdList = list(prodDict.values())
    if len(tempProdList) == 0:
        print()
        print("No stationary to sort!")
    else:
        prodListLength = len(tempProdList)
        print()
        for i in range(prodListLength - 1): # worst-case scenario (most iterations)
            for j in range(prodListLength - i - 1): # take away the previous iterations
                if tempProdList[j].get_category() < tempProdList[j+1].get_category(): #check if need swap elemnts
                    tempProdList[j], tempProdList[j+1] = tempProdList[j+1], tempProdList[j] # swap element positions

            print(f"Pass {i+1}:")
            print("-----------------------------------------------")
            for k in range(len(tempProdList)):
                print(f"Product_ID: {tempProdList[k].get_Prod_id()}")
            print("-----------------------------------------------")
        
        print()
        print("---------------Bubble Sorted Stationary List---------------")
        for product in range(len(tempProdList)):
            print(f"Product ID: {tempProdList[product].get_Prod_id()}")
            print(f"Product Name: {tempProdList[product].get_ProdName()}")
            print(f"Product Category: {tempProdList[product].get_category()}")
            print(f"Brand: {tempProdList[product].get_brand()}")
            print(f"Supplier Year: {tempProdList[product].get_Supplier_since()}")
            print("-----------------------------------------------")

        prodDict = {}
        for stationary in tempProdList:
            prodDict[stationary.get_Prod_id()] = stationary # clear previous dict and update with sorted values
                

def insertionSortStationary():
    global prodDict
    tempProdList = list(prodDict.values())
    if len(tempProdList) == 0:
        print()
        print("No stationary to sort!")
    else:
        prodListLength = len(tempProdList)
        print()
        for i in range(1, prodListLength): # start from 2nd element cos assume 1st is sorted already
            keyElement = tempProdList[i] # store the current element to be compared
            j = i - 1 # index of the element on the left

            while j >= 0 and keyElement.get_brand() < tempProdList[j].get_brand(): # compare key with elements on the left
                tempProdList[j + 1] = tempProdList[j] # move element to the right
                j -= 1 # decrement j until it reaches index 0 and breaks out of the loop

            tempProdList[j + 1] = keyElement # put back keyElement where it belongs
            
            print(f"Pass {i}:")
            print("-----------------------------------------------")
            for k in range(len(tempProdList)):
                print(f"Product_ID: {tempProdList[k].get_Prod_id()}")
            print("-----------------------------------------------")

        print()
        print("---------------Insertion Sorted Stationary List---------------")
        for product in range(len(tempProdList)):
            print(f"Product ID: {tempProdList[product].get_Prod_id()}")
            print(f"Product Name: {tempProdList[product].get_ProdName()}")
            print(f"Product Category: {tempProdList[product].get_category()}")
            print(f"Brand: {tempProdList[product].get_brand()}")
            print(f"Supplier Year: {tempProdList[product].get_Supplier_since()}")
            print("-----------------------------------------------")

        prodDict = {}
        for stationary in tempProdList:
            prodDict[stationary.get_Prod_id()] = stationary # clear previous dict and update with sorted values

def selectionSortStationary(): # Sort by descending order of Prod_id
    global prodDict
    tempProdList = list(prodDict.values())
    if len(tempProdList) == 0:
        print()
        print("No stationary to sort!")
    else:
        prodListLength = len(tempProdList)
        print()
        for i in range(prodListLength):
            largestItemIndex = i
            for j in range(i+1, prodListLength):
                if tempProdList[j].get_Prod_id() > tempProdList[largestItemIndex].get_Prod_id():
                    largestItemIndex = j
            tempProdList[i], tempProdList[largestItemIndex] = tempProdList[largestItemIndex], tempProdList[i]

            print(f"Pass {i + 1}:")
            print("-----------------------------------------------")
            for k in range(len(tempProdList)):
                print(f"Product_ID: {tempProdList[k].get_Prod_id()}")
            print("-----------------------------------------------")

        print()
        print("---------------Selection Sorted Stationary List---------------")
        for product in range(len(tempProdList)):
            print(f"Product ID: {tempProdList[product].get_Prod_id()}")
            print(f"Product Name: {tempProdList[product].get_ProdName()}")
            print(f"Product Category: {tempProdList[product].get_category()}")
            print(f"Brand: {tempProdList[product].get_brand()}")
            print(f"Supplier Year: {tempProdList[product].get_Supplier_since()}")
            print("-----------------------------------------------")

def mergeSortStationary():
    pass

def restockProduct():
    pass

def numberOfStockArrival():
    pass

def serviceNextRestock():
    pass

def restockMenu():
    while True:
        print()
        print("Restocking Menu: ")
        print("1. Enter new stock arrival.")
        print("2. View Number of stock arrival.")
        print("3. Service next restock in queue.")
        print("0. Return to Main Menu.")
        print()

        try:
            choice = int(input("Please select one: "))
            if choice == 1:
                restockProduct()
            elif choice == 2:
                numberOfStockArrival()
            elif choice == 3:
                serviceNextRestock()
            elif choice == 0:
                print()
                print("Exiting to main menu...")
                break
            else:
                print()
                print("Invalid choice. Please enter either [0, 1, 2 or 3].")
        except ValueError:
            print()
            print("Please enter a valid number as a choice.")

def setRecordsPerRow():
    pass

def populateData(): # populate data and for testing purposes
    global prodDict
    prodDict = {}
    newStudA = Stationary("PD1020", "Pastel Art Paper", "Paper", "Faber-Castell", 2021, 2000)
    prodDict[newStudA.get_Prod_id()] = newStudA
    newStudA = Stationary("PD1025", "Mars Lumograph Drawing Pencils", "Pencils", "Staedtler", 2022, 320)
    prodDict[newStudA.get_Prod_id()] = newStudA
    newStudA = Stationary("PD1015", "Water color Pencils", "Pencils", "Faber-Castell", 2011, 150)
    prodDict[newStudA.get_Prod_id()] = newStudA
    newStudA = Stationary("PD1050", "Noris 320 fiber tip pen", "Pens", "Staedtler", 2021, 350)
    prodDict[newStudA.get_Prod_id()] = newStudA
    newStudA = Stationary("PD1001", "Copier Paper (A4) 70GSM", "Paper", "PaperOne", 2021, 1500)
    prodDict[newStudA.get_Prod_id()] = newStudA
    newStudA = Stationary("PD1033", "Scientific Calculator FX-97SG X", "Calculator", "Casio", 2022, 50)
    prodDict[newStudA.get_Prod_id()] = newStudA
    newStudA = Stationary("PD1005", "Pop Bazic File Separator Clear", "Office Supplies", "Popular", 2000, 500)
    prodDict[newStudA.get_Prod_id()] = newStudA
    print()
    print("Data populated!")
    return prodDict # return the populated data as dictionary
                

def menu():
    global prodDict
    while True:
        print()
        print("------------------Stationary Management System------------------")
        print("1. Add a new Stationary.")
        print("2. Display all Stationary.")
        print("3. Sort Stationary via Bubble Sort on Category.")
        print("4. Sort Stationary via Insertion Sort on Brand.")
        print("5. Sort Stationary via Selection Sort on Prod_id.")
        print("6. Sort Stationary via Merge Sort on Category follow by Stock in ascending order.")
        print("7. Go to Restocking Menu.")
        print("8. Set number of records per row to display.")
        print("9. Populate data.")
        print("0. Exit program.")
        print()

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
                selectionSortStationary()
            elif choice == 6:
                mergeSortStationary()
            elif choice == 7:
                restockMenu()
            elif choice == 8:
                setRecordsPerRow()
            elif choice == 9:
                prodDict = populateData()
            elif choice == 0:
                print()
                print("Program quit. Good bye!")
                print()
                break
            else:
                print()
                print("Invalid choice. Please enter either [0, 1, 2, 3, 4 or 9].")
        except ValueError:
            print()
            print("Please enter a valid number.")


menu()