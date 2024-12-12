import psycopg2
import csv

# Function to connect to the database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="phonebook",
            user="postgres",
            password="1234",
            host="localhost",
            port="5433"
        )
        print("Connected to the database.")
        return conn
    except psycopg2.Error as e:
        print("Database connection error:", e)
        return None

# Function to create the table if it doesn't exist
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            phone_number VARCHAR(15) UNIQUE NOT NULL
        );
        """)
        conn.commit()
        print("Table PhoneBook created.")
    except psycopg2.Error as e:
        print("Error creating table:", e)

# Function to insert data
def insert_data(conn, first_name, last_name, phone_number):
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO PhoneBook (first_name, last_name, phone_number)
        VALUES (%s, %s, %s);
        """, (first_name, last_name, phone_number))
        conn.commit()
        print(f"Data inserted: {first_name} {last_name}, {phone_number}.")
    except psycopg2.Error as e:
        print("Data insertion error:", e)

# Function to upload data from CSV file
def upload_from_csv(conn, file_path):
    try:
        cursor = conn.cursor()
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header
            for row in reader:
                cursor.execute("""
                INSERT INTO PhoneBook (first_name, last_name, phone_number)
                VALUES (%s, %s, %s)
                ON CONFLICT (phone_number) DO NOTHING;
                """, (row[0], row[1], row[2]))
        conn.commit()
        print(f"Data from {file_path} loaded successfully.")
    except Exception as e:
        print("Error loading data from CSV:", e)

# Function to update data
def update_data(conn):
    try:
        id_to_update = int(input("Enter the ID of the record to update: "))
        print("Select what you want to update:")
        print("1. First Name")
        print("2. Last Name")
        print("3. Phone Number")
        choice = input("Your choice: ")

        if choice == "1":
            new_value = input("Enter the new first name: ")
            column = "first_name"
        elif choice == "2":
            new_value = input("Enter the new last name: ")
            column = "last_name"
        elif choice == "3":
            new_value = input("Enter the new phone number: ")
            column = "phone_number"
        else:
            print("Invalid choice.")
            return

        cursor = conn.cursor()
        query = f"UPDATE PhoneBook SET {column} = %s WHERE id = %s;"
        cursor.execute(query, (new_value, id_to_update))
        conn.commit()
        print(f"Data updated: ID={id_to_update}, {column}={new_value}.")
    except Exception as e:
        print("Error updating data:", e)

# Function to delete data
def delete_data(conn):
    try:
        id_to_delete = int(input("Enter the ID of the record to delete: "))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM PhoneBook WHERE id = %s;", (id_to_delete,))
        conn.commit()
        print(f"Record with ID={id_to_delete} deleted.")
    except Exception as e:
        print("Error deleting data:", e)

# Function to select and display data
def select_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PhoneBook order by 1;")
        rows = cursor.fetchall()
        print("Data in the table:")
        for row in rows:
            print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Phone: {row[3]}")
    except psycopg2.Error as e:
        print("Error fetching data:", e)

# Menu function to manage data
def menu(conn):
    while True:
        print("\nMenu:")
        print("1. Show all records")
        print("2. Add a new record")
        print("3. Load data from CSV")
        print("4. Update a record")
        print("5. Delete a record")
        print("6. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            select_data(conn)
        elif choice == "2":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            insert_data(conn, first_name, last_name, phone_number)
        elif choice == "3":
            file_path = input("Enter the path to the CSV file: ")
            upload_from_csv(conn, file_path)
        elif choice == "4":
            update_data(conn)
        elif choice == "5":
            delete_data(conn)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, try again.")

# Main function
if __name__ == "__main__":
    connection = connect_to_db()  # Establish connection
    if connection:
        create_table(connection)  # Ensure the table exists
        menu(connection)  # Launch menu
        connection.close()
        print("Database connection closed.")
