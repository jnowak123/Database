import mysql.connector

conn = mysql.connector.connect(user='root', password='1234',
                            host='127.0.0.1',
                            database='classicmodels')
cursor = conn.cursor()

loggedUser = None
def mainMenu():
    global loggedUser
    print()
    print('Witaj w programie obsługującym dane firmy.')
    
    while loggedUser is None:
        login = input('Aby się zalogowac podaj numer pracownika: ')
        pswd = input('Podaj haslo: ')
        stmt = "SELECT firstname FROM employees WHERE extension = '{}' and employeeNumber = '{}';".format(pswd, login)
        print(stmt)
        cursor.execute(stmt)
        loggedUser = cursor.fetchone()
        if loggedUser is not None:
            # User does not exist
            break
    print('Witaj', loggedUser[0])
    print('(D)odaj zamówienie')
    print('(W)yświetl ...')
    print('(Z)akończ')
    opt = input("Podaj znak by wybrać opcję: ").strip().upper()
    if opt == 'D':
        createOrder()
    elif opt == 'W':
        pass
    elif opt == 'Z':
        print('Zamykam')
        quit()
    else:
        print('Komenda nieznana')
        mainMenu()

def createOrder():
    customer = chooseCustomer()
    products = chooseProducts()
    makeOrder(customer, products)
    mainMenu()

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

        filterCustomers(opt[2:])
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
    stmt = "SELECT customerNumber, customerName FROM customers WHERE LOWER(customerName) LIKE '%{0}%';".format(filterPhrase)
    print(stmt)
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
    products.append(chooseProduct())
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
            return [product for product in products if product is not None] 
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
            code, name, description, msrp = product
            print('Dodano produkt {0} o kodzie {1}, z ceną sugerowaną {2}'.format( name, code,msrp))
            
            amount = input('Podaj liczbę sztuk: ')
            while not amount.isnumeric():
                amount = input('Niepoprawna wartość. Podaj liczbę sztuk: ')
            
            price = input('Podaj cenę: ')
            while not price.isnumeric():
                price = input('Niepoprawna wartość. Podaj cenę: ')
            return (code, amount, price)
            

def showAllProducts():
    stmt = "SELECT productCode, productName, productDescription FROM products;"
    cursor.execute(stmt)
    for row in cursor.fetchall():
        print(row)

def filterProducts(filterPhrase):
    stmt = """SELECT productCode, productName, productDescription FROM products 
            WHERE LOWER(productName)
             LIKE '%{0}%' OR LOWER(productDescription)
             LIKE '%{0}%';""".format(filterPhrase)
    cursor.execute(stmt)
    for row in cursor.fetchall():
        print(row)

def getProduct(productCode):
    stmt = "SELECT productCode, productName, productDescription, MSRP FROM products WHERE productCode = '{0}';".format(productCode)
    cursor.execute(stmt)
    return cursor.fetchone()

def makeOrder(customer, products):
    maxOrderNumberStmt = """SELECT MAX(orderNumber) from orders;"""
    cursor.execute(maxOrderNumberStmt)
    maxOrderNumber = cursor.fetchone()
    orderNumber = maxOrderNumber[0] + 1
    orderStmt = """INSERT INTO orders (orderNumber, customerNumber, orderDate, requiredDate, status)
                VALUES
            ({0}, {1}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP + interval '7' day, 'In Process');""".format(orderNumber, customer)
    cursor.execute(orderStmt)
    orderDetails = []
    for index, (code, amount, price) in enumerate(products, start=1):
        orderDetails.append((orderNumber, code, price, amount, index))
    detailsStmt = """INSERT INTO orderDetails (orderNumber, productCode, priceEach, quantityOrdered, orderLineNumber) 
                    VALUES 
                    (%s, %s, %s, %s, %s)"""
    cursor.executemany(detailsStmt, orderDetails)
    conn.commit()



mainMenu()

