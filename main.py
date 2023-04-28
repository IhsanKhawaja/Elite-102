import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'PocketWizard1!')
cursor = connection.cursor()

def check(ID):
    Query = (f"SELECT Balance FROM bank_system Where ID = {ID}")
    cursor.execute(Query)
    for item in cursor:
        print(item)

def create(name, balance, admin, cred):
    addData = (f"INSERT INTO bank_system (Name, Balance, Admin, Credit) VALUES( {name}, {balance}, {admin}, {cred})")
    cursor.execute(addData)
    connection.commit()

def show():
    testQuery = ("SELECT * FROM bank_system")
    cursor.execute(testQuery)
    for item in cursor:
        print(item)

show()

connection.close()