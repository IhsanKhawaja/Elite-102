import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'PocketWizard1!')
cursor = connection.cursor()

def check_balance(ID):
    Query = (f"SELECT Balance FROM bank_system Where ID = {ID}")
    cursor.execute(Query)
    for item in cursor:
        return item

def check_cred(ID):
    Query = (f"SELECT Credit FROM bank_system Where ID = {ID}")
    cursor.execute(Query)
    for item in cursor:
        return item

def create(name, balance, admin, cred):
    addData = (f"INSERT INTO bank_system (Name, Balance, Admin, Credit) VALUES( {name}, {balance}, {admin}, {cred})")
    cursor.execute(addData)
    connection.commit()

def show():
    testQuery = ("SELECT * FROM bank_system")
    cursor.execute(testQuery)
    for item in cursor:
        print(item)

def sign_in(ID):
    Query = (f"SELECT * FROM bank_system Where ID = {ID}")
    cursor.execute(Query)
    for item in cursor:
        return item

def get_name(ID):
    Query = (f"SELECT Name FROM bank_system Where ID = {ID}")
    cursor.execute(Query)
    for item in cursor:
        return item
    
def update_balance(ID, Extra):
    Update = (f"UPDATE bank_system SET Balance = Balance + {int(Extra)} WHERE ID = {ID};")
    cursor.execute(Update)

def update_credit(ID, Extra):
    Update = (f"UPDATE bank_system SET Credit = Credit + {int(Extra)} WHERE ID = {ID};")
    cursor.execute(Update)


print("Welcome to your banking server! Here are the following accounts-")
show()
ID = input(f"To continue, please enter your User ID or create a new account (CA): ").upper()
Name = None
while True:
    if(ID == "CA"):
        ID = 0
        Name = input("Name: ")
        Name = "'" + Name + "'"
        create(Name, input("Balance: "), False, input("Credit: "))
        testQuery = ("SELECT * FROM bank_system")
        cursor.execute(testQuery)
        for item in cursor:
            ID += 1
        print(f"Your User ID is: {ID}")
        break
    elif (sign_in(ID) != None):
        Name = str(get_name(ID))
        response = input(f"Name: {Name[2:-3]}, ID: {ID}. Is this you? (y/n) ")
        if(response == "y"):
            break
    else:
        print("User ID doesn't exist")
    ID = input("Please enter a new ID or create a new account (CA): ")

print("\nCB - check balance\nCC - check credit score\nexit - quit the program\nhelp - print out all the commands\nUB - updates your balance with whatever value you enter\nUC - updates your Credit with whatever value you enter\n")

while(True):
    response = input("What would you like to do?\n").upper()
    if (response == "EXIT"):
        break
    elif (response == "CB"):
        print(f"your balance is ${str(check_balance(ID))[1:-2]}\n")
    elif (response == "CC"):
        print(f"you have a credit score of {str(check_cred(ID))[1:-2]}\n")
    elif (response == "UB"):
        response = input("Would you like to deposit or withdraw (d/w): ").upper()
        if (response == "D"):
            update_balance(ID, input("Enter the amount you would like to add: "))
        else:
            update_balance(ID, -int(input("Enter the amount you would like to Withdraw: ")))
        print(f"your new balance is ${str(check_balance(ID))[1:-2]}\n")
    elif (response == "UC"):
        response = input("Is your credit score increasing or decreasing (i/d): ").upper()
        if (response == "I"):
            update_credit(ID, input("Enter the amount you would like to add: "))
        else:
            update_credit(ID, -int(input("Enter the amount you would like to reduce: ")))
        print(f"your new credit score is {str(check_cred(ID))[1:-2]}\n")
    elif(response == "HELP"):
        print("\nCB - check balance\nCC - check credit score\nexit - quit the program\nhelp - print out all the commands\nUB - updates your balance with whatever value you enter\nUC - updates your Credit with whatever value you enter\n")

connection.close()