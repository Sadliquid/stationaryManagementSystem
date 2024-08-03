# Name: Joshua Long Yu Xuan
# Student Admin Number: 230627W
# Tutorial Group: IT2153-01

from Stationary import Stationary # Stationary class
from RestockDetail import RestockDetail # RestockDetail class (for products to be restocked)
from RestockingQ import RestockingQ # Queue ADT

prodDict = {} # global dictionary
deliveryQueue = RestockingQ() # global queue
recordsPerRow = 1 # default value


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
    global recordsPerRow
    global prodDict
    if len(prodDict) == 0:
        print()
        print("There are currently no products in the system!")
    else:
        productStringList = [] # list to store each product as a string
        for stationary in prodDict.values():
            product = f"""
                Product ID: {stationary.get_Prod_id()}
                Product Name: {stationary.get_ProdName()}
                Product Category: {stationary.get_category()}
                Brand: {stationary.get_brand()}
                Supplier Year: {stationary.get_Supplier_since()}
                Stock: {stationary.get_Stock()}
            """
            productStringList.append(clean_and_split(product))
        display_in_chunks(productStringList, recordsPerRow) # display the products in chunks of records per row


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
        
        productStringList = [] # list to store each product as a string
        for stationary in tempProdList:
            product = f"""
                Product ID: {stationary.get_Prod_id()}
                Product Name: {stationary.get_ProdName()}
                Product Category: {stationary.get_category()}
                Brand: {stationary.get_brand()}
                Supplier Year: {stationary.get_Supplier_since()}
                Stock: {stationary.get_Stock()}
            """
            productStringList.append(clean_and_split(product))
        display_in_chunks(productStringList, recordsPerRow) # display the products in chunks of records per row

        prodDict = {} # clear the previous dict
        for stationary in tempProdList:
            prodDict[stationary.get_Prod_id()] = stationary # update dictionary with bubble-sorted values
                

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

        productStringList = [] # list to store each product as a string
        for stationary in tempProdList:
            product = f"""
                Product ID: {stationary.get_Prod_id()}
                Product Name: {stationary.get_ProdName()}
                Product Category: {stationary.get_category()}
                Brand: {stationary.get_brand()}
                Supplier Year: {stationary.get_Supplier_since()}
                Stock: {stationary.get_Stock()}
            """
            productStringList.append(clean_and_split(product))
        display_in_chunks(productStringList, recordsPerRow) # display the products in chunks of records per row

        prodDict = {}
        for stationary in tempProdList: # clear previous dict
            prodDict[stationary.get_Prod_id()] = stationary # update dictionary with insertion-sorted values

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

        productStringList = [] # list to store each product as a string
        for stationary in tempProdList:
            product = f"""
                Product ID: {stationary.get_Prod_id()}
                Product Name: {stationary.get_ProdName()}
                Product Category: {stationary.get_category()}
                Brand: {stationary.get_brand()}
                Supplier Year: {stationary.get_Supplier_since()}
                Stock: {stationary.get_Stock()}
            """
            productStringList.append(clean_and_split(product))
        display_in_chunks(productStringList, recordsPerRow) # display the products in chunks of records per row

        prodDict = {} # clear the previous dict
        for stationary in tempProdList:
            prodDict[stationary.get_Prod_id()] = stationary # update dictionary with selection-sorted values

def mergeSortStationary():
    global prodDict
    tempProdList = list(prodDict.values())
    if len(tempProdList) == 0:
        print()
        print("No stationary to sort!")
    else:
        def mergeSort(tempProdList):
            if len(tempProdList) > 1:
                mid = len(tempProdList) // 2 # get the median index
                leftHalf = tempProdList[:mid]
                rightHalf = tempProdList[mid:]

                mergeSort(leftHalf) # recursive call to split the left half until it reaches smallest size
                mergeSort(rightHalf) # recursive call to split the right half until it reaches smallest size

                i = j = k = 0 # i for leftHalf, j for rightHalf, k for tempProdList

                while i < len(leftHalf) and j < len(rightHalf):
                    if leftHalf[i].get_category() < rightHalf[j].get_category() or (
                        leftHalf[i].get_category() == rightHalf[j].get_category() and
                        leftHalf[i].get_Stock() < rightHalf[j].get_Stock()):
                        tempProdList[k] = leftHalf[i]
                        i += 1
                    else:
                        tempProdList[k] = rightHalf[j]
                        j += 1
                    k += 1

                while i < len(leftHalf): # if there are still elements in the leftHalf, add it to tempProdList
                    tempProdList[k] = leftHalf[i]
                    i += 1
                    k += 1

                while j < len(rightHalf): # if there are still elements in the rightHalf, add it to tempProdList
                    tempProdList[k] = rightHalf[j]
                    j += 1
                    k += 1

                print("Pass:")
                print("-----------------------------------------------")
                for item in tempProdList:
                    print(f"Product_ID: {item.get_Prod_id()}")
                print("-----------------------------------------------")

        mergeSort(tempProdList)

        productStringList = [] # list to store each product as a string
        for stationary in tempProdList:
            product = f"""
                Product ID: {stationary.get_Prod_id()}
                Product Name: {stationary.get_ProdName()}
                Product Category: {stationary.get_category()}
                Brand: {stationary.get_brand()}
                Supplier Year: {stationary.get_Supplier_since()}
                Stock: {stationary.get_Stock()}
            """
            productStringList.append(clean_and_split(product))
        display_in_chunks(productStringList, recordsPerRow) # display the products in chunks of records per row

        prodDict = {} # clear the previous dict
        for stationary in tempProdList:
            prodDict[stationary.get_Prod_id()] = stationary  # update dictionary with merge-sorted values

def restockProduct():
    global prodDict
    global deliveryQueue
    productKeysList = list(prodDict.keys())
    while True:
        restockProdID = str(input("Enter Product ID to restock: "))
        searchResult = sequentialSearch(productKeysList, restockProdID)
        if searchResult != -1:
            restockQuantity = int(input("Enter quantity to restock: "))
            restockDetail = RestockDetail(restockProdID, restockQuantity)
            deliveryQueue.enqueue(restockDetail)
            print()
            print("Restocking arival queued successfully!")
            break
        else:
            print()
            print("Invalid Product ID. Please try again!")
            print()

def numberOfStockArrival():
    global deliveryQueue
    print()
    print(f"Number of restocking in queue: {deliveryQueue.len()}")

def serviceNextRestock():
    global prodDict
    global deliveryQueue
    if deliveryQueue.isEmpty():
        print()
        print("No restocking in queue.")
    else:
        restockDetail = deliveryQueue.dequeue() # pop the first restock in queue (FIFO)
        productKeysList = list(prodDict.keys()) # list of all product IDs
        restockProdID = restockDetail.get_Prod_id()
        restockQuantity = restockDetail.get_quantity()
        searchResult = sequentialSearch(productKeysList, restockProdID) # search for the product ID to check if it exists
        if searchResult != -1:
            print()
            print("Display pending stock arrival: ")
            print("--------------------------------")
            print(f"Product ID: {restockProdID}")
            print(f"Product Name: {prodDict[restockProdID].get_ProdName()}")
            print(f"Product Category: {prodDict[restockProdID].get_category()}")
            print(f"Brand: {prodDict[restockProdID].get_brand()}")
            print(f"Supplier Year: {prodDict[restockProdID].get_Supplier_since()}")
            print(f"Stock remaining: {prodDict[restockProdID].get_Stock()}")
            print("--------------------------------")
            print(f"New Stock: {restockQuantity}")
            print("--------------------------------")
            
            print()
            print(f"Remaining restocks in queue: {deliveryQueue.len()}")
            print()
            
            proceedWithRestocking = input("Proceed with restocking? (Y/N): ")
            if proceedWithRestocking.upper() == "Y":
                prodDict[restockProdID].set_Stock(prodDict[restockProdID].get_Stock() + restockQuantity) # update stock
                print() 
                print(f"Product ID {prodDict[restockProdID].get_Prod_id()} updated stock: {prodDict[restockProdID].get_Stock()}")
            elif proceedWithRestocking.upper() == "N":
                deliveryQueue.enqueue(restockDetail) # put the restock back to the end of the queue
                print("Restocking not serviced.")
            else:
                deliveryQueue.enqueue(restockDetail) # put the restock back to the end of the queue
                print("Invalid choice. Restocking cancelled.")
        else:
            print()
            print("Invalid Product ID. Restocking not serviced.")

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
    global recordsPerRow
    print()
    while True:
        numberOfRecords = input("Enter number of records per row to display (Max 3 rows): ")
        try:
            numberOfRecords = int(numberOfRecords)
            if 3 >= numberOfRecords > 0:
                recordsPerRow = numberOfRecords
                print()
                print(f"Number of records per row set to: {recordsPerRow}")
                break
            elif numberOfRecords > 3:
                print()
                print("Displaying more than 3 records per row may cause the text to be misaligned. Please enter a number less than or equal to 3.")
                print()
            else:
                print()
                print("Please enter a number thats greater than 0.")
                print()
        except ValueError:
            print()
            print("Please enter a valid number.")

def clean_and_split(product_string): # split each product string into lines and remove leading/trailing spaces
    return [line.strip() for line in product_string.strip().split('\n')]

def display_in_chunks(strings, num_per_row, spacing=' ', column_width=45, start=0):
    def truncate_text(text, width):
        return text if len(text) <= width else text[:width-3] + '...' # truncate text if it exceeds column width, remove 3 characters for '...'
    
    if start >= len(strings):
        return # prevent maximum recursion depth exceeded error
    
    chunk = strings[start:start + num_per_row]
    transposed_text = list(zip(*chunk)) # convert rows to columns, so thy can be formatted into "chunks"
    print()
    for line in transposed_text:
        formatted_line = [f"{truncate_text(field, column_width):<{column_width}}" for field in line] # ":" specifies the start of the format specifier, "<" left-aligns the text
        print(spacing.join(formatted_line))
    print()
    
    display_in_chunks(strings, num_per_row, spacing, column_width, start + num_per_row) # print next chunk recursively. "start" incrrements by num_per_row each time

def sequentialSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1


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