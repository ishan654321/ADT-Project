import mysql.connector
from mysql.connector import Error

def create_connection():
    """Establishes a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',        # Update with your username
            password='password',# Update with your password
            database='economic_data'  # Update with your database name
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful!")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def fetch_all_data(cursor, table_name):
    """Fetches all data from a specified table."""
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    return cursor.fetchall()

def insert_into_country_gdp(cursor, data):
    """Inserts a record into the Country_GDP table."""
    query = """
    INSERT INTO Country_GDP (Number, Country, GDP_PPP_2022) 
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, data)

def insert_into_tourism_data(cursor, data):
    """Inserts a record into the tourism_data table."""
    query = """
    INSERT INTO tourism_data (country, tourists_in_millions, receipts_in_billions, 
                              receipts_per_tourist, percentage_of_gdp)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)

def insert_into_unemployment_data(cursor, data):
    """Inserts a record into the unemployment_data table."""
    query = """
    INSERT INTO unemployment_data (country, unemployment_rate) 
    VALUES (%s, %s)
    """
    cursor.execute(query, data)

def insert_into_cost_of_living_data(cursor, data):
    """Inserts a record into the cost_of_living_data table."""
    query = """
    INSERT INTO cost_of_living_data (country, cost_index, monthly_income, purchasing_power_index) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, data)

def main():
    connection = create_connection()
    if not connection:
        return
    
    cursor = connection.cursor()
    
    while True:
        print("\nMenu:")
        print("1. View all data from a table")
        print("2. Insert data into Country_GDP")
        print("3. Insert data into tourism_data")
        print("4. Insert data into unemployment_data")
        print("5. Insert data into cost_of_living_data")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            table_name = input("Enter the table name (Country_GDP, tourism_data, unemployment_data, cost_of_living_data): ")
            try:
                data = fetch_all_data(cursor, table_name)
                print(f"\nData from {table_name}:")
                for row in data:
                    print(row)
            except Error as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            try:
                number = int(input("Enter Number: "))
                country = input("Enter Country: ")
                gdp_ppp_2022 = input("Enter GDP_PPP_2022 (or NULL): ")
                gdp_ppp_2022 = float(gdp_ppp_2022) if gdp_ppp_2022.upper() != 'NULL' else None
                insert_into_country_gdp(cursor, (number, country, gdp_ppp_2022))
                connection.commit()
                print("Data inserted into Country_GDP successfully.")
            except Error as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            try:
                country = input("Enter Country: ")
                tourists = float(input("Enter Tourists (in millions): "))
                receipts = float(input("Enter Receipts (in billions): "))
                per_tourist = int(input("Enter Receipts per Tourist: "))
                percentage = float(input("Enter Percentage of GDP: "))
                insert_into_tourism_data(cursor, (country, tourists, receipts, per_tourist, percentage))
                connection.commit()
                print("Data inserted into tourism_data successfully.")
            except Error as e:
                print(f"Error: {e}")
        
        elif choice == '4':
            try:
                country = input("Enter Country: ")
                rate = float(input("Enter Unemployment Rate: "))
                insert_into_unemployment_data(cursor, (country, rate))
                connection.commit()
                print("Data inserted into unemployment_data successfully.")
            except Error as e:
                print(f"Error: {e}")
        
        elif choice == '5':
            try:
                country = input("Enter Country: ")
                cost_index = float(input("Enter Cost Index: "))
                income = float(input("Enter Monthly Income: "))
                power_index = float(input("Enter Purchasing Power Index: "))
                insert_into_cost_of_living_data(cursor, (country, cost_index, income, power_index))
                connection.commit()
                print("Data inserted into cost_of_living_data successfully.")
            except Error as e:
                print(f"Error: {e}")
        
        elif choice == '6':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
