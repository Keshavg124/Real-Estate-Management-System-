import sqlite3
conn = sqlite3.connect("real_estate.db") 
cur = conn.cursor() 
 
cur.execute(""" 
CREATE TABLE IF NOT EXISTS properties ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    location TEXT, 
    price REAL, 
    status TEXT 
) 
""") 
conn.commit() 
class RealEstateSystem: 
 
    def add_property(self, name, location, price, status): 
        cur.execute( 
            "INSERT INTO properties (name, location, price, status) VALUES (?, ?, ?, ?)", 
            (name, location, price, status) 
        ) 
        conn.commit() 
        print("Property added successfully!") 
 
    def view_properties(self): 
        cur.execute("SELECT * FROM properties") 
        rows = cur.fetchall() 
        for r in rows: 
            print(r) 
        print() 
 
    def search_property(self, pid): 
        cur.execute("SELECT * FROM properties WHERE id=?", (pid,)) 
        result = cur.fetchone() 
        if result: 
            print("Property Found:", result) 
        else: 
            print("Property not found.")
        print() 
 
    def update_property(self, pid, name, location, price, status): 
        cur.execute( 
            "UPDATE properties SET name=?, location=?, price=?, status=? WHERE id=?", 
            (name, location, price, status, pid) 
        ) 
        conn.commit() 
        print("Property updated!\n") 
 
    def delete_property(self, pid): 
        cur.execute("DELETE FROM properties WHERE id=?", (pid,)) 
        conn.commit() 
        print("Property deleted!\n")
        system = RealEstateSystem() 
 
while True: 
    print("\n--- Real Estate Management System ---") 
    print("1. Add Property") 
    print("2. View All Properties") 
    print("3. Search Property") 
    print("4. Update Property") 
    print("5. Delete Property") 
    print("6. Exit") 
 
    choice = input("Enter choice: ") 
 
    if choice == "1": 
        name = input("Name: ") 
        location = input("Location: ") 
        price = float(input("Price: ")) 
        status = input("Status (Available/Sold/Rented): ") 
        system.add_property(name, location, price, status) 
 
    elif choice == "2": 
        system.view_properties() 
 
    elif choice == "3": 
        pid = input("Enter Property ID: ") 
        system.search_property(pid) 
 
    elif choice == "4": 
        pid = input("Property ID: ") 
        name = input("New Name: ") 
        location = input("New Location: ") 
        price = float(input("New Price: ")) 
        status = input("New Status: ") 
        system.update_property(pid, name, location, price, status) 
 
    elif choice == "5": 
        pid = input("Enter Property ID to delete: ") 
        system.delete_property(pid) 
 
    elif choice == "6": 
        print("Exiting...") 
        break 
 
    else: 
        print("Invalid choice, try again.")  
