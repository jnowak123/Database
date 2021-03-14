import mysql.connector

conn = mysql.connector.connect(user='root', password='1234',
                            host='127.0.0.1',
                            database='classicmodels')
cursor = conn.cursor()

orderhistory = []

def mainMenu():
    while True:
        print()
        print('Witaj w programie obsługującym dane firmy.')
        print('(D)odaj zamówienie')
        print('(W)yświetl ostatnie zamówienia')
        print('(Z)akończ')
        opt = input("Podaj znak by wybrać opcję: ").strip().upper()
        if opt == 'D':
            createOrder()
        elif opt == 'W':
            print(orderhistory)
        elif opt == 'Z':
            print('Zamykam')
            quit()
        else:
            print('Komenda nieznana')

def createOrder():
    products = chooseProducts()
    customer = chooseCustomer()
    makeOrder(customer, products)

def chooseCustomer():
    print()
    print('Wybierz klienta podając jego identyfikator. Możesz też:')
    print('(W)yświetlić wszystkich klientów')
    print('(F)iltrować po nazwie klienta. Przykład: F abc')
    print('(C)ofnąć się do głównego menu')
    opt = input('Podaj identyfikator lub znak by wybrać opcję: ').strip().upper()
    if opt == 'W':
        showAllCustomers()
    elif opt.startswith('F '):
        filterCustomers(opt.split()[1])
    elif opt.isnumeric():
        if validateCustomer(opt):
            print('Podano poprawny identyfikator')
            return opt
        else:
            print('Niepoprawny identyfikator')
    elif opt == 'C':
        mainMenu()
    else:
        print('Komenda nieznana')
    return chooseCustomer()

def showAllCustomers():
    stmt = "SELECT customerNumber, customerName FROM CUSTOMERS;"
    cursor.execute(stmt)
    for row in cursor.fetchall():
        print(row)

def filterCustomers(filterPhrase):
    stmt = "SELECT customerNumber, customerName FROM customers WHERE customerName LIKE '%{0}%';".format(filterPhrase)
    cursor.execute(stmt)
    for row in cursor.fetchall():
        print(row)


def validateCustomer(customerNumber):
    stmt = "SELECT customerNumber FROM customers WHERE customerNumber = {0};".format(customerNumber)
    cursor.execute(stmt)
    if not cursor.fetchone():
        return False
    return True
        
def chooseProducts():
    products = []
    while True:
        print()
        print('(D)odaj kolejny produkt')
        print('(Z)rób zamówienie')
        print('(C)ofnij się do głównego menu')
        opt = input('Podaj znak by wybrać opcję: ').strip().upper()
        if opt == 'D':
            product = chooseProduct()
            #UWAGA product może być pustym obiektem (mogło się nie udać jego wyciągnięcie) 
            products.append(product)
        elif opt == 'Z':
            filterProducts()
        elif opt == 'C':
            mainMenu() #To nie jest nalepsze rozwiązanie bo wywołanie chooseProducts pozostaje na stosie wywołań
        else:
            print('Komenda nieznana')

def chooseProduct():
    print()
    print('Wybierz produkt podając jego kod. Możesz też:')
    print('(W)yświetlić wszystkie produkty')
    print('(F)iltrować po nazwie lub opisie produktu. Przykład: F abc')
    print('(C)ofnąć się do głównego menu')
    opt = input('Podaj identyfikator lub znak by wybrać opcję: ').strip().upper()
    if opt == 'W':
        showAllProducts()
    elif opt.startswith('F '):
        filterProducts(opt.split()[1])
    else:
        product = getProduct(opt)
        if not product:
            print('Niepoprawny kod')
        else:
            print(product)
            #W przypadku kiedy produkt o zadanym kodzie znajdował się w bazie należy dopytać użytkownika 
            # o liczbę sztuk i cenę. Warto też wcześniej wyśwetić mu szczegóły wybranego produktu, np, proponowaną cenę jego sprzedaży (msrp)
            # Przykład z pobieraniem od użytkownika liczby sztuk:
            amount = input('Podaj liczbę sztuk: ')
            while not amount.isnumeric():
                amount = input('Niepoprawna wartość. Podaj liczbę sztuk: ')
            price = input('Podaj cenę: ')
            while not price.isnumeric():
                price = input('Niepoprawna wartość. Podaj cenę: ')


def showAllProducts():
    stmt = "SELECT productCode, productName, productDescription FROM PRODUCTS;"
    cursor.execute(stmt)
    for row in cursor.fetchall():
        print(row)

def filterProducts(filterPhrase):
    stmt = "SELECT productCode, productName, productDescription FROM products WHERE produktName LIKE '%{0}%'; or productDescription LIKE '%{0}%';".format(filterPhrase, filterPhrase)
    cursor.execute(stmt)
    for row in cursor.fetchall():
        print(row)

def getProduct(productCode):
    stmt = "SELECT productCode, productName, productDescription, msrp, quantityinstock FROM products WHERE productCode = {0};".format(productCode)
    cursor.execute(stmt)
    mylist = []
    for row in cursor.fetchall():
        mylist.append(row)
    return mylist
    #Funkcja ma na celu zwrócenie tupla reprezentującego produkt o zadanym productCode.
    # Może się zdarzyć, że taki nie istnieje. Jakie dane powinny się zawrzeć w tuplu zależy od tego, 
    # co będzie potrzebne przy tworzeniu zamówienia 
   

def makeOrder(customer, products):
    stmt = "SELECT max(ordernumber) FROM orders"
    cursor.execute(stmt)
    orderNumber = cursor.fetchone()[0] +1 

    orderhistory.append([orderNumber, customer, products])
    
    orderStmt = """INSERT INTO orders (orderNumber, customerNumber, orderDate, requiredDate, status)
                VALUES
            (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP + interval '7' day, 'In Process');"""
    #Przekazywany w drugim argumencie metody execute tuple, jest rozpakowywany do kolejnych placeholderów zapytania. 
    #W powyższym przykładzie dwóch %s
    cursor.execute(orderStmt, (orderNumber, customer))
    orderDetails = []
    
    #TODO przygotowanie orderDetails na podstawie produktów. 
    # orderLineNumber jest po prostu numerkiem kolejnych pozycji zamóienia (1, 2, 3 itd)
    #
    #

    detailsStmt = """INSERT INTO orderDetails (orderNumber, productCode, priceEach, quantityOrdered, orderLineNumber) 
                    VALUES 
                    (%s, %s, %s, %s, %s)"""
    #funkcja executeMany  potrafi przyjąć w drugim argumencie listę tupli i wywołać zapytanie wielokrotnie 
    # przekazując kolejne tuple kolejnym wywołanym zapytaniom. 
    # Tuple ten jest wtedy rozpakowywanyw miejsce placeholderów do wzorca zapytania                      
    cursor.executemany(detailsStmt, orderDetails)

    # Po dokonaniu insertów należy je zatwierdzić (zamknąć transakcję). 
    # Bez tej operacji dokonane zmiany nie byłyby widoczne w bazie danych dla innych z nią połączeń.
    # commit wywołuje się na połćzeniu a nie na kursorze! 
    conn.commit() 

mainMenu()

