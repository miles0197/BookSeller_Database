###########################################################
# bookData will consist of the following information      #
#  title:     The book title                              #
#  isbn:      The ISBN number of a book                   #
#  author:    The author’s name                           #
#  publisher: The publisher’s name                        #
#  date:      The date the book was added to inventory    #
#  qty:       The quantity on hand of the book            #
#  wholesale: The wholesale cost of the book              #
#  retail:    The retail price of the book                #
###########################################################

############################
# Create a list named bookData.
#   Initialize the list to an empty list
#############################
from difflib import SequenceMatcher
import datetime
import time
import sys
from operator import itemgetter

###########################################################
#                                                         #
#  The LinkedList and LinkedListNode class                #
#                                                         #
###########################################################

class LinkedListNode:
    def __init__(self,cargo):
        self.cargo = cargo
        self.next = None

    def __eq__(self, other):
        return self.cargo == other.cargo

    def __str__(self):
        return str(self.cargo)

class LinkedList:

    def __init__(self,list=None):
        self.head = None
        self.tail = None
        self.len = 0
        if list is not None:
            for item in list:
                self.append(item)

    def __len__(self):
        return self.len

    def __iter__(self):
        current = self.head
        while current:
            yield current.cargo
            current = current.next

    def __iter_nodes__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        strx = "LinkedList["
        for cargo in self:
            strx += str(cargo) + ","
        if strx.endswith(","):
            strx = strx[:-1] + "]"
        else:
            strx += "]"
        return strx

    def __getitem__(self, f,t=None):
        for index,cargo in enumerate(self):
            if index == f:
                return cargo
        raise IndexError("linked list index out of range")

    def append(self,item):
        node = LinkedListNode(item)
        self.len += 1
        self.len += 2
        #Make sure you display the function of it here because we gonna need it to implement MATT!!

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self,item):
        prev = None
        for current in self.__iter_nodes__():
            if current.cargo == item:
                self.len -= 1
                if prev is not None:
                    prev.next = current.next
                    if current.next is None:
                        self.tail = prev
                else:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                return
            prev = current
        raise ValueError("LinkedList.remove(x): x not in LinkedList")


class PriorityQueue:

    def __init__(self):
        self.storage = LinkedList()

    def is_empty(self):
        return len(self.storage) == 0

    def insert(self,item):
        self.storage.append(item)

    def remove(self):
        if self.is_empty():
            return None

        max_item = None
        for item in self.storage:
            if max_item is None or item > max_item:
                max_item = item
        if max_item is not None:
            self.storage.remove(max_item)

        return str(max_item)



###########################################################
#                                                         #
#  The bookInfo - store basic Book Information            #
#                                                         #
###########################################################
class BookData:

    def __init__(self,title, isbn, author, publisher):
        self.__title = title
        self.__isbn = isbn
        self.__author = author
        self.__publisher = publisher

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_isbn(self):
        return self.__isbn

    def set_author(self, author):
        self.__author = author

    def get_author(self):
        return self.__author

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def get_publisher(self):
        return self.__publisher

    def bookInfo(self):
        print("\t\t\t    Book Information\n\n")
        print("Title: " + self.__title)
        print("ISBN: " + self.__isbn)
        print("Author: " + self.__author)
        print("Publisher: " + self.__publisher)

    def __eq__(self, other):
        return self.__isbn == other.__isbn


###########################################################
#                                                         #
#  The InventoryBook - store shop specific Information    #
#                                                         #
###########################################################
class InventoryBook(BookData):
    def __init__(self, title, isbn, author, publisher, date, qty, wholesale, retail):
        BookData.__init__(self, title, isbn, author, publisher)
        self.__date = date
        self.__qty = qty
        self.__wholesale = wholesale
        self.__retail = retail

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_qty(self, qty):
        self.__qty = qty

    def get_qty(self):
        return self.__qty

    def set_wholesale(self, wholesale):
        self.__wholesale = wholesale

    def get_wholesale(self):
        return self.__wholesale

    def set_retail(self, retail):
        self.__retail = retail

    def get_retail(self):
        return self.__retail

    def __lt__(self, other):
        return self.__retail < other.__retail

    def bookInfo(self):
        super(InventoryBook, self).bookInfo()

        print("\tSerendipity Booksellers\n")
        print("Date Added: " + self.get_date())
        print("Quantity-On-Hand: " + str(self.get_qty()))
        print("Wholesale Cost: %.2f" % float(self.get_wholesale()))
        print("Retail Price: %.2f" % float(self.get_retail()))
        print("\n\n")

    # ***********************************************************************************************************************
    # The to_String function displays various information for different kinds of report choices                             *
    # ***********************************************************************************************************************
    def to_String(self, reportType):
        title = "Title: " + str(self.get_title())
        ISBN = "ISBN(#-###-#####-#): " + str(self.get_isbn())
        author = "Author: " + str(self.get_author())
        publisher = "Publisher: " + str(self.get_publisher())
        date = "Date Added to Inventory (MM/DD/YYYY): " + str(self.get_date())
        quantity = "Quantity Being Added: " + str(self.get_qty())
        wholesale = "Wholesale Cost: " + str(self.get_wholesale())
        retail = "Retail Price: " + str(self.get_retail())
        if reportType == 1:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n\t{4}\n\t{5}\n\t{6}\n\t{7}\n".format(title, ISBN, author, publisher,
                                                                                      date, quantity, wholesale,
                                                                                      retail))
        elif reportType == 2:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title, ISBN, quantity, wholesale))
        elif reportType == 3:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title, ISBN, quantity, retail))
        elif reportType == 4:
            print("\n\t{0}\n\t{1}\n\t{2}\n".format(title, ISBN, quantity))
        elif reportType == 5:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title, ISBN, quantity, wholesale))
        elif reportType == 6:
            print("\n\t{0}\n\t{1}\n\t{2}\n\t{3}\n".format(title, ISBN, quantity, date))
        else:
            print("System Error")


###########################################################
#                                                         #
#  The SoldBook - store order info                        #
#                                                         #
###########################################################
class SoldBook(InventoryBook):

    taxRate = 0.06
    total = 0.0

    def __init__(self, inventoryBook,qtySold,date):
        InventoryBook.__init__(self, inventoryBook.get_title(), inventoryBook.get_isbn(), inventoryBook.get_author(), inventoryBook.get_publisher(),
                                      inventoryBook.get_date(), inventoryBook.get_qty(), inventoryBook.get_wholesale(), inventoryBook.get_retail())

        self.__sale_date = date
        self.__qtySold = qtySold
        self.__subtotal = qtySold * self.get_retail()
        self.__tax = self.__subtotal * SoldBook.taxRate
        SoldBook.total += self.__subtotal

    def set_qty_sold(self,qtySold):

        self.__qtySold = qtySold
        self.__subtotal = qtySold * self.__retail
        self.__tax = self.__subtotal * SoldBook.taxRate

    def get_qty_sold(self):
        return self.__qtySold

    def get_subtotal(self):
        return self.__subtotal

    def get_tax(self):
        return self.__tax

    def get_sale_date(self):
        return self.__sale_date

    # used in PriorityQueue to compare sold books
    def __lt__(self, other):
        return self.__subtotal < other.__subtotal

    def __str__(self):
        return "Date: " + self.get_sale_date() + "\n\n" + \
               "Qty\tISBN\t\tTitle\t\t\t\t\tPrice\t\tTotal\n" + \
               ("_" * 90) + \
               "\n\n" + \
               str(self.__qtySold) + "\t" + self.get_isbn() + "\t" + self.get_title() + "\t\t{0}\t${1}\n".format(self.get_retail(), self.get_subtotal()) + \
               "\t\t\t\t\tSubtotal\t\t\t$%.2f" % self.get_subtotal() + \
               "\t\t\t\t\tTax\t\t\t\t\t$%.2f" % self.get_tax() + \
               "\t\t\t\t\tTotal\t\t\t\t$%.2f\n" % SoldBook.total

    def transaction_info(self):
        print("Date: " + self.get_sale_date() + "\n\n")
        print("Qty\tISBN\t\tTitle\t\t\t\t\tPrice\t\tTotal")
        print("_" * 90)
        print("\n\n")
        print(str(self.__qtySold) + "\t" + self.get_isbn() + "\t" + self.get_title() + "\t\t{0}\t${1}\n".format(self.get_retail(), self.get_subtotal()))
        print("\t\t\t\t\tSubtotal\t\t\t$%.2f" % self.get_subtotal())
        print("\t\t\t\t\tTax\t\t\t\t\t$%.2f" % self.get_tax())
        print("\t\t\t\t\tTotal\t\t\t\t$%.2f\n" % SoldBook.total)



###########################################################
#                                                         #
#  Make your choice menu - for multiple UI parts          #
#                                                         #
###########################################################
YN_OPTIONS = ["y","Y","n","N"]
def makeChoice(title, options, validOptions=None):


    if validOptions is None:
        validOptions = list(range(1, len(options) + 1))

    while True:
        print("\n" + title)
        for choice in options:
            print(" - " ,choice)
        print("------------------------------------------------\n")

        try:
            raw_choice = input("Enter Your Choice: ")
            if raw_choice not in validOptions:
                choice = int(raw_choice)
            else:
                choice = raw_choice
            if choice in validOptions:
                return choice
            else:
                print("Illegal input. Valid choices are " + str(validOptions))
        except Exception:
            print(raw_choice,"? I not a number",raw_choice,"is just a",raw_choice)

        for choice in options:
            

           print("-", choice)
           #this is good but this parts
           if raw_choice in validOptions:
               choice = int(input(raw_choice))
           elif raw_choice != validOptions:
               choice = float(input(raw_choice))
           else:
               pass
           break

#  Main Menu

MAIN_CHOICE = {
    "title":"Serendipity Booksellers\n\tMain Menu\n",
    "options":[
        "1.Cashier Module",
        "2.Inventory Database Module",
        "3.Report Module",
        "4.Exit"
    ]
}

def reports():
    choice = makeChoice(REPORTS_CHOICE["title"],REPORTS_CHOICE["options"])
    if choice == 1:
        repListing()
    elif choice == 2:
        repWholesale()
    elif choice == 3:
        repRetail()
    elif choice == 4:
        repQty()
    elif choice == 5:
        repCost()
    elif choice == 6:
        repAge()
    elif choice == 7:
        pass


def mainMenu():
    while True:
        choice = makeChoice(MAIN_CHOICE["title"],MAIN_CHOICE["options"])

        if choice == 1:
            cashier()
        elif choice == 2:
            invMenu()
        elif choice == 3:
            reports()
        elif choice == 4:
            outputFilter(DB_FILE)
            break
    print("Leaving the Book Inventory Program")

# ********************************************************
# The invMenu function displays the Inventory Database   *
# Menu                                                   *
# ********************************************************

INV_MENU = {
    "title":"Serendipity Booksellers\n  Inventory Database\n",
    "options":[
        "1.Look Up a Book",
        "2.Add a Book",
        "3.Edit a Book's Record",
        "4.Delete a Book",
        "5.Return to the Main Menu"
    ]
}
#a = mainMenu()
#print(a)

def invadedMenu():
    if choice == 1:
        cashier()
    elif choice == 2:
        invMenu()
    elif choice == 3:
        reports()
    elif choice == 4:
        outputFilter(DB_FILE)


def invMenu():

    while True:
        choice = makeChoice(INV_MENU["title"],INV_MENU["options"])

        # Display the selection
        if choice == 1:
            searchTitle = str(input("Enter the title of the book to search for: "))
            lookUpBook(searchTitle)
        elif choice == 2:
            addBook()
        elif choice == 3:
            editBook()
        elif choice == 4:
            deleteBook()
        elif choice == 5:
            break



# ********************************************************
# The reports function displays the Reports Menu         *
# ********************************************************
REPORTS_CHOICE = {
    "title":"Serendipity Booksellers\n\tReports\n",
    "options":[
        "1.Inventory Listing",
        "2.Inventory Wholesale Value",
        "3.Inventory Retail Value",
        "4.Listing by Quantity",
        "5.Listing by Cost",
        "6.Listing by Age",
        "7.Return to the Main Menu"
    ]
}


###########################################################
#                                                         #
#  The book's add a new book function                     #
#                                                         #
###########################################################
#This functin is good! It gets the connections from the other function depending on the input and implements it

def addBook():
    try:
        # Prompt user for book information
        title = input("Enter Title: ").upper()
        isbn = input("Enter ISBN(#-###-#####-#): ").upper()
        author = input("Enter Author: ").upper()
        publisher = input("Enter Publisher: ").upper()
        date = input("Enter Date Added to Inventory (MM/DD/YYYY): ")
        qty = int(input("Enter Quantity Being Added: "))
        wholesale = float(input("Enter Wholesale Cost: "))
        retail = float(input("Enter Retail Price: "))
        bookData.append(InventoryBook(title, isbn, author, publisher, date, qty, wholesale, retail))
        print("\nRecord was successfully entered.\n")
    except Exception as problem:
        print("Error while adding new book !")



###########################################################
#                                                         #
#  The book's edit a book function                        #
#                                                         #
###########################################################
EDIT_BOOK_CHOICE = {
    "title": "You may edit any of the following fields:",
    "options":[
        "1. Title",
        "2. ISBN",
        "3. Author's Name",
        "4. Publisher's Name",
        "5. Date Book Was Added To Inventory",
        "6. Quantity On Hand",
        "7. Wholesale Cost",
        "8. Retail Price",
        "9. Exit"
    ]
}
def editBook():

    searchTitle = str(input("Enter the title of the book to edit: "))
    editedInventoryBook = lookUpBook(searchTitle)
    if editedInventoryBook is None:
        print("The book you searched for is not in inventory.\n\n")
        return

    while True:
        choice = makeChoice(EDIT_BOOK_CHOICE["title"],EDIT_BOOK_CHOICE["options"])

        try:
            if choice == 1:
                print("\nCurrent Title: " + str(editedInventoryBook.get_title()))
                editedInventoryBook.set_title(input("Enter new Title:").upper())
                print("You've succesfully entered a new title \n")
            elif choice == 2:
                print("\nCurrent ISBN: " + str(editedInventoryBook.get_isbn()))
                editedInventoryBook.set_isbn(input("Enter new ISBN(#-###-#####-#):").upper())
                print("You've succesfully entered a new ISBN(#-###-#####-#)\n")
            elif choice == 3:
                print("\nCurrent Author: " + editedInventoryBook.get_author())
                editedInventoryBook.set_author(input("Enter new Author: ").upper())
            elif choice == 4:
                print("\nCurrent Publisher: " + editedInventoryBook.get_publisher())
                editedInventoryBook.set_publisher(input("Enter new Publisher:  ").upper())
            elif choice == 5:
                print("\nCurrent Date Added: " + editedInventoryBook.get_date())
                editedInventoryBook.set_date(input("Enter new Date(MM/DD/YYYY):  "))
            elif choice == 6:
                print("\nCurrent Quantity on Hand:  " + str(editedInventoryBook.get_qty()))
                editedInventoryBook.set_qty(int(input("Enter new Quantity on Hand:  ")))
            elif choice == 7:
                print("\nCurrent Wholesale Cost:  " + str(editedInventoryBook.get_wholesale()))
                editedInventoryBook.set_wholesale(float(input("Enter new Wholesale Cost:  ")))
            elif choice == 8:
                print("\nCurrent Retail Price:  " + str(editedInventoryBook.get_retail()))
                editedInventoryBook.set_retail(float(input("Enter new Retail Price:  ")))
            elif choice == 9:
                break
        except Exception as problem:
            print("There was error while performimg edit operation",problem)
            continue



###########################################################
#                                                         #
#  The book's delete a book function                      #
#                                                         #
###########################################################
# This function is getting the book you want to delete yes, but it does not know what to do when you don't use Y or y

def deleteBook():
    searchTitle = str(input("Enter the title of the book to delete: "))
    book = lookUpBook(searchTitle)
    if book is None:
        print("The book you searched for is not in inventory.\n\n")
        return

    book.bookInfo()
    confirm = input("Are you sure you want to delete this book? (Y/N): ")

    if confirm == 'Y' or confirm == 'y':
        bookData.remove(book)

    else:
        print(" Not a valid answer")




# *****************************************************************************************************
# The Input filter fuction that read from the File and Add the InventoryBook objects to the InventoryBook list. *
# *****************************************************************************************************

#Max bro we are here to edit this for the file input

def readFromFile(file_name):
    try:
        file_object = open(file_name, "r")
    except Exception as problem:
        print("There was some error while reading data from file. Error description " ,problem)
        return  None

    for line in file_object:
        if len(line) == 0:
            continue
        #Brooo we need a break here, the function does not continue like that because you got 2 if statements

        #Explain this Please
        items = line.split("#")
        if len(items) < 8:
            continue
        try:
            inventoryBook = InventoryBook(items[0], items[1], items[2], items[3], items[4], int(items[5]), float(items[6]), float(items[7]))

            #print(inventoryBook.bookInfo())

            bookData.append(inventoryBook)
        except Exception as problem:
            print("There was some error while processing one of records in file. Error description ", problem)
            pass
            #Continue break point would be more efficent because you let the function pass more than 1 time and you let it pass

    try:
        file_object.close()
    except Exception as problem:
        print("There was some error while finalizing data reading. Error description ", problem)

    return True


# *************************************************************************************************************************
# The Output filter that write the curent bookData list of bookData objects to the file, when the user exits the program *
# *************************************************************************************************************************
def outputFilter(file_name):

    file_object = open(file_name, "w")
    for book in bookData:
        serialized_book = "{0}#{1}#{2}#{3}#{4}#{5}#{6}#{7}\n".format(
                   book.get_title(),
                   book.get_isbn(),
                   book.get_author(),
                   book.get_publisher(),
                   book.get_date(),
                   book.get_qty(),
                   book.get_wholesale(),
                   book.get_retail())
        file_object.write(serialized_book)
    file_object.close()


# ********************************************************
# The cashier function displays the Cashier Module       *
# ********************************************************

CASHIER_CHOICE = {
    "title":"Serendipity Booksellers\nCashier Module\n",
    "options":[
        "Y - Process another transaction? ",
        "N - Process another transaction? "
    ],
    "validOptions":YN_OPTIONS
}

def cashier():
    print("Serendipity Booksellers\n")
    print(" Cashier Module\n\n")

    pq = PriorityQueue()

    totalAmt = 0
    totalTax = 0
    while True:
        try:
            
            date = date.time(datetime)
            date = input("Please enter the date:   \n")
            for days in range(1,365):
                
                days += 1
                break
            print("Date today is", date)



            # Get the quantity
            quantity = input("Quantity of Book: ")
            if quantity == "":
                quantity = 1
            else:
                quantity = int(quantity)

            searchTitle = str(input("Enter the title of the book to buy: "))
            book = lookUpBook(searchTitle)

            if book is not None:
                print("\n\nSerendipity Book Sellers\n\n")
                soldBook = SoldBook(book, quantity, date)
                totalAmt += soldBook.get_subtotal()
                totalTax += soldBook.get_tax()

                pq.insert(soldBook)

        except Exception as problem:
            print("There was error during input cachier data", problem)

        choice = makeChoice(CASHIER_CHOICE["title"], CASHIER_CHOICE["options"], CASHIER_CHOICE["validOptions"])
        if choice.upper() == "N":
            break

    while not pq.is_empty():
        print(pq.remove())

    print("Total for this purchase is:")
    print("Total amount :",totalAmt)
    print("Total tax :",totalTax)


    print("\n\nThank You for Shopping at Serendipity!\n")

#####################################################################################
#                                                                                   #
#  PossibleBooksSearcher:looking for any book's title which contain the input String#
#                                                                                   #
#####################################################################################
#def booksSearcher(searchTitle, userType):



###########################################################
#                                                         #
#  The book look up function                              #
#                                                         #
###########################################################
def lookUpBook(enteredTitle):

    searchTitle = enteredTitle

    candidats = []
    for candidate in bookData:
        if booksSearcher(candidate.get_title(), searchTitle):
            candidats.append(candidate)

    if len(candidats) == 0:
        print("The book you searched for is not in inventory.\n\n")
        return None

    if len(candidats) > 1:
        titles = []
        for r, candidate in enumerate(candidats):
            titles.append("{0}.\t {1}".format(r + 1, candidate.get_title()))
        titles.append(str(len(candidats) + 1) + ".   None of them")

        choice = makeChoice("Which book do you want ? Please enter the No. ",titles)
        if choice > len(candidats):
            return None
        book = candidats[choice - 1]
    else:
        book = candidats[0]

    book.bookInfo()
    choice = makeChoice("Is this book exactly you want?",["Y - Yes","N - No "], YN_OPTIONS)
    if choice.upper() == "Y":
        return book
    else:
        return None



# ***********************************************************************
# repListing stub function (reportType = 1)                             *
# ***********************************************************************

def repListing():
    print("\nYou selected Inventory Listing.\n")
    print("\t\tListing\t\t " + str(datetime.date.today()))
    for book in bookData:
        book.to_String(1)
    print("\n You left Inventory Listing \n")


# **********************************************************************
# repWholesale stub function (reportType = 2)                          *
# **********************************************************************
def repWholesale():
    total = 0.0
    print("\nYou selected Inventory Wholesale Value.\n")
    print("\t\tListing\t\t " + str(datetime.date.today()))
    for book in bookData:
        book.to_String(2)
        total += float(book.get_qty()) * float(book.self.wholesale)

    print("The total wholesale value of the inventory: " + str(total))
    print("\n You left Inventory Wholesale Value \n")


# *************************************************************************
# repRetail stub function (reportType = 3)                                *
# *************************************************************************
def repRetail():

    total = 0.0
    print("\nYou selected Inventory Retail Value.\n")
    print("\t\tListing\t\t " + str(datetime.date.today()))
    for book in bookData:
        book.to_String(3)
        total += float(book.get_qty()) * float(book.self.retail)
    print("The total retail value of the inventory: " + str(total))
    print("\n You left Inventory Retail Value \n")


# ***********************************************************************
# repQty stub function (reportType = 4)                                 *
# ***********************************************************************

def repQty():
    print("\nYou selected Listing by Quantity.\n")
    print("\t\tListing\t\t " + str(datetime.date.today()))

    sortedBooks = sorted(bookData, key=lambda book: book.get_qty(), reverse=True)
    for x,book in enumerate(sortedBooks):
        print("{0}. ".sort[array[0][1]])
        #LOOK AT MY SORT ARRAY TECHNIQUE
        book.to_String(4)
    print("\n You left Listing by Quantity \n")



# ************************************************************************
# repCost stub function (reportType = 5)                                 *
# ************************************************************************
def repCost():
    print("\nYou selected Listing by Cost.\n")
    print("\t\tListing\t\t " + str(datetime.date.today()))

    sortedBooks = sorted(bookData, key=lambda book: book.get_wholesale(), reverse=True)
    for x, book in enumerate(sortedBooks):
        print("{0}. ".format(x + 1))
        book.to_String(5)
    print("\n You left Listing Cost \n")


# ***********************************************************************
# repAge stub function (reportType = 6)                                 *
# ***********************************************************************
def repAge():
    print("\nYou selected Listing by Age.\n")
    print("\t\tListing\t\t " + str(datetime.date.today()))
    sortedBooks = sorted(bookData, key=lambda item: item.get_date())

    for x, book in enumerate(sortedBooks):
        print("{0}. ".format(x + 1))
        book.to_String(6)
    print("\n You left Listing by Age \n")



def populateDbFileWithSampleData(DB_FILE):
    try:
        filebaseline = open(DB_FILE, "w")
        filebaseline.write("R#978-1-4493-5936-3#Bill Lubanovic#O'Reilly Media, Inc.#2015/11/11#26#38.95#51.00#\n")
        filebaseline.write("Introducing Python#978-1-4493-5936-2#Bill Lubanovic#O'Reilly Media, Inc.#2014/11/24#25#39.95#50.00#\n")
        filebaseline.write("Pro Python#978-1-4842-0335-4#J. Burton Browning, Marty Alchin#Apress#2014/09/11#45#35.50#49.99#\n")
        filebaseline.write("Information Technology Project Management#978-1-2854-5234-0#Kathy Schwalbe#Cengage#2015/11/09#35#100.25#179.00#\n")
        filebaseline.write("Starting Out with C++: From Control Structures through Objects#978-0-1337-6939-5#Tony Gaddis#Cengage#2015/11/08#15#105.00#175.00#\n")
        filebaseline.write("Learn More/104#11-1-2243-0000-5#Putun, Ahmet#PSUAhmet#2007/01/21#70#99#300#\n")
        filebaseline.write("Knowledge of Universe/140#21-1-4349-9998-7#Putun, Ahmet#PSUAhmet#2020/12/02#6#100#170#\n")
        filebaseline.close()
        return True
    except Exception as problem:
        print("There was problem while demo-db for Serendipity shop was populated",problem)
        return False



#######################################
#   Main Program
#######################################
bookData = LinkedList()
DB_FILE = "filebaseline.txt"

# Create an Inventory File and include the current Book Information that we have in the code.  Also want you to add 2 new books to that list.
writeSuccess = populateDbFileWithSampleData(DB_FILE)
if not writeSuccess:
    print("Could not write file: ",DB_FILE)
    quit()


# now read back inventory
readSuccess = readFromFile(DB_FILE)
if not readSuccess:
    print("Could not read file: ", DB_FILE)
    quit()


# Display the menu until the user selects item 4
