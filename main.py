import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(host="127.0.0.1", user="root", password="root")
cur = conn.cursor()
def databasetable():
    cur.execute("create database if not exists CSprojects")
    cur.execute("use CSprojects") 
    cur.execute("create table if not exists services(servicecode INT AUTO_INCREMENT PRIMARY KEY, service VARCHAR(100) NOT NULL, StdDisc INT NOT NULL, EmpDisc INT NOT NULL, SeniorDisc INT NOT NULL, ActiveUsers INT NOT NULL DEFAULT 0, BasePrice DECIMAL(10, 2) NOT NULL)")
    cur.execute("create table if not exists users (UserID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, username VARCHAR(100) NOT NULL, password VARCHAR(255) NOT NULL, subscription1 INT NULL, subscription2 INT NULL, subscription3 INT NULL, subscription4 INT NULL, subscription5 INT NULL, StdDisc INT NOT NULL DEFAULT 2, EmpDisc INT NOT NULL DEFAULT 2, SeniorDisc INT NOT NULL DEFAULT 2, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, CONSTRAINT fk_users_subscription1 FOREIGN KEY (subscription1) REFERENCES services(servicecode), CONSTRAINT fk_users_subscription2 FOREIGN KEY (subscription2) REFERENCES services(servicecode), CONSTRAINT fk_users_subscription3 FOREIGN KEY (subscription3) REFERENCES services(servicecode), CONSTRAINT fk_users_subscription4 FOREIGN KEY (subscription4) REFERENCES services(servicecode), CONSTRAINT fk_users_subscription5 FOREIGN KEY (subscription5) REFERENCES services(servicecode))")
   

databasetable()

def show_users(cur):
    cur.execute("SELECT UserID, name, username, password FROM users ORDER BY UserID")
    print('*'*50)
    print("\nUsers:\nId \t| Name \t| Username \t| Password")
    for row in cur:
        print(f"{row[0]} \t| {row[1]} \t| {row[2]} \t| {row[3]}")
    print('*'*50)

def show_services(cur):
    print('*'*50)
    print("\nServices:\nService Code \t| Service Name \t| Base Price")
    cur.execute("SELECT servicecode, service, BasePrice FROM services ORDER BY servicecode")
    for row in cur:
        print(f"{row[0]} \t| {row[1]} \t| ${row[2]}")
    print('*'*50)

def nooly(balue):
    while True:
        try:
            return int(input(balue))
        except ValueError:
            print("Please enter a number.")

def addservices():
    cur.execute("INSERT INTO services (service, StdDisc, EmpDisc, SeniorDisc, ActiveUsers, BasePrice) VALUES ('Streaming Service', 10, 15, 20, 0, 9.99),\n('Cloud Storage', 5, 10, 15, 0, 4.99),\n('PW lakshya access', 15, 20, 25, 0, 14.99),\n('Music Subscription', 10, 15, 20, 0, 7.99),\n('Fitness Pro+ App', 5, 10, 15, 0, 5.99)")
    conn.commit()
    print("Sample services successfully loaded into the Registery.")

def addusers():
    cur.execute("SELECT COUNT(*) FROM services")
    service_count = 0
    for row in cur:
        service_count = row[0]
        
    if service_count < 5:
        print("Adding sample services...")
        addservices()

    cur.execute("INSERT INTO users (name, username, password, subscription1, subscription2, subscription3, subscription4, subscription5, StdDisc, EmpDisc, SeniorDisc) VALUES ('Aarav Sharma', 'aarav1', 'pass1', 1, 3, NULL, NULL, NULL, 1, 2, 2),\n('Priya Patel', 'priya2', 'pass2', 2, 4, 5, NULL, NULL, 2, 1, 2),\n('Rohan Das', 'rohan3', 'pass3', 3, NULL, NULL, NULL, NULL, 2, 2, 1),\n('Ananya Iyer', 'ananya4', 'pass4', 1, 5, NULL, NULL, NULL, 1, 2, 2),\n('Kabir Singh', 'kabir5', 'pass5', 4, 2, 1, NULL, NULL, 2, 1, 2),\n('Diya ', 'diya6', 'pass6', 3, 5, NULL, NULL, NULL, 2, 2, 1),\n('Arjun Verma', 'arjun7', 'pass7', 2, NULL, NULL, NULL, NULL, 1, 2, 2),\n('Isha Gupta', 'isha8', 'pass8', 1, 4, 3, 5, NULL, 2, 1, 2),\n('Dev Reddy', 'dev983', 'pass9', 5, 2, NULL, NULL, NULL, 2, 2, 1),\n('Meera Nair', 'meera10', 'pass10', 4, 1, NULL, NULL, NULL, 1, 2, 2)")
    conn.commit()

def manage_users(conn, cur):
    while True:
        print('*'*50)
        print("\nUsers Control Menu")
        print("1. View users")
        print("2. Delete user")
        print("3. Create random sample users") 
        print("4. Back")
        choice = nooly("Enter choice: ")
        if choice == 1:
            show_users(cur)
        elif choice == 2:
            user_id = input("Enter user ID: ").strip()
            cur.execute(f"DELETE FROM users WHERE UserID = {user_id}")
            conn.commit()
            print("User removed.")
        elif choice == 3:
            addusers()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

def manage_services(conn, cur):
    while True:
        print('-'*20, end='')
        print("Services Setup", end='')
        print('-'*20)
        print("1. View services")
        print("2. Create service")
        print("3. Create random sample services")
        print("4. Back")
        choice = nooly("Enter choice: ")
        if choice == 1:
            show_services(cur)
        elif choice == 2:
            service_name = input("Service name: ").strip()
            base_price = input("Base price: ").strip()
            std_disc = input("Student discount: ").strip()
            emp_disc = input("Employee discount: ").strip()
            senior_disc = input("Senior discount: ").strip()
            cur.execute(f"INSERT INTO services (service, StdDisc, EmpDisc, SeniorDisc, ActiveUsers, BasePrice) VALUES ('{service_name}', {std_disc}, {emp_disc}, {senior_disc}, 0, {base_price})")
            conn.commit()
            print("Service created successfully.")
        elif choice == 3:
            addservices()
        elif choice == 4:
            break
        else:
            print("Invalid choice.")

def billing_flow(conn, cur):
    name = input("Please enter your full name: ").strip()
    username = input("Please choose a preferred username: ").strip()
    password = input("Please choose a password for this account: ").strip()

    student = nooly("Are you a student? (1 : Yes, 2 : No): ")
    employee = nooly("Are you an internal company employee? (1 : Yes, 2 : No): ")
    senior = nooly("Are you a senior citizen? (1 : Yes, 2 : No): ")


    cur.execute(f"INSERT INTO users (name, username, password, StdDisc, EmpDisc, SeniorDisc) VALUES ('{name}', '{username}', '{password}', {student}, {employee}, {senior})")
    conn.commit()

    cur.execute("SELECT UserID FROM users ORDER BY UserID DESC")
    user_id = 0
    for rows in cur:
        if user_id == 0:
            user_id = rows[0]

    cur.execute("SELECT servicecode, service, BasePrice, StdDisc, EmpDisc, SeniorDisc FROM services ORDER BY servicecode")
    print("\n--- Official Service Registery ---")
    
    number = 1
    for rows in cur:
        print(f"[{number}] {rows[1]} - ${rows[2]}")
        number = number + 1

    selected = []
    total = 0.0
    names = []

    while len(selected) < 5:
        choice = nooly("Please enter the number of the service to add (or type 0 to finalize selection): ")
        if choice == 0:
            break
        
        cur.execute(f"SELECT servicecode, service, BasePrice, StdDisc, EmpDisc, SeniorDisc FROM services WHERE servicecode = {choice}")
        
        row = []
        for rows in cur:
            row = rows
            
        if len(row) == 0:
            print("That entry was not recognized. Please check the Registery numbers and try again.")
            continue

        discount = 0
        if student == 1 and row[3] > discount:
            discount = row[3]
        if employee == 1 and row[4] > discount:
            discount = row[4]
        if senior == 1 and row[5] > discount:
            discount = row[5]

        price = float(row[2]) * (1 - discount / 100)
        total += price
        names.append(f"{row[1]} (${price:.2f})")
        selected.append(str(row[0]))
        print("Service successfully added to your pending layout.")

    if len(selected) == 0:
        print("No selections were registered. Terminating the session.")
        return

    while len(selected) < 5:
        selected.append("NULL")
    now = datetime.now()
    invoice = str(user_id) + "_" + name.replace(" ", "_") + "_" + str(now.year) + str(now.month) + str(now.day)
    
    cur.execute(f"UPDATE users SET subscription1 = {selected[0]}, subscription2 = {selected[1]}, subscription3 = {selected[2]}, subscription4 = {selected[3]}, subscription5 = {selected[4]} WHERE UserID = {user_id}")
    conn.commit()

    print(f"\n========================================\nINVOICE REFERENCE: {invoice}\nAccount Name: {name}\nAccount ID: {username}\nLine Items: {'-'.join(names)}\nGrand Total: ${total:.2f}\n========================================\nTransactions logged and database entry verified.")


while True:
    print("\nMain Menu")
    print("1. Users")
    print("2. Services")
    print("3. Billing")
    print('4. Wipe database and its contents (Run with precaution !)')
    print("5. Exit")
    try:
        choice = nooly("Enter choice: ")
    except ValueError:
        print("Invalid numeric choice. Please enter a number.")
        continue
    if choice == 1:
        manage_users(conn, cur)
    elif choice == 2:
        manage_services(conn, cur)
    elif choice == 3:
        billing_flow(conn, cur)
    elif choice == 4:
        cur.execute("DELETE FROM users")
        cur.execute("ALTER TABLE users AUTO_INCREMENT = 1")
        cur.execute("DELETE FROM services")
        cur.execute("ALTER TABLE services AUTO_INCREMENT = 1")
        conn.commit()
        print("Database wiped.")
        databasetable()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")

cur.close()
conn.close()