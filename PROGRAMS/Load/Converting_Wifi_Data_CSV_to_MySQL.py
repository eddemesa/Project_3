import csv
import mysql.connector
from datetime import datetime

# MySQL connection parameters
mysql_host = 'localhost'  # Change if your MySQL server is hosted elsewhere
mysql_database = 'mydb'  # Replace with your database name
mysql_user = 'root'  # Replace with your MySQL username
mysql_password = 'KyleElle$0313'  # Replace with your MySQL password

# CSV file path
csv_file_path = \
    '/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_wifi_data.csv'

# Establishing a connection to the MySQL database
connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
    )

# Create a cursor object
cursor = connection.cursor()

# Drop the table if it exists
drop_table_query = 'DROP TABLE IF EXISTS Wifi_data_Transactions'
cursor.execute(drop_table_query)
print("Table `Wifi_data_Transactions` dropped if it existed")

# Create a new table
create_table_query = '''
    CREATE TABLE Wifi_data_Transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    SSID VARCHAR(255),
    Level INT,
    Date DATE,
    Time TIME
    )
    '''
cursor.execute(create_table_query)
print("Table `Wifi_data_Transactions` created")

# Read data from CSV and insert into MySQL table
with open(csv_file_path, mode='r', encoding='ISO-8859-1') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        # Select only the desired columns
        ssid = row['SSID']
        level = row['level']

        # Assuming the column is named 'Date'
        original_date = row['Date']
        # Remove any leading/trailing whitespace
        original_date = original_date.strip()

        # Convert the string to a datetime object
        date_obj1 = datetime.strptime(original_date, "%m/%d/%Y")

        try:
            formatted_date = date_obj1.strftime("%Y/%m/%d")
            # Output the formatted date
            # print(formatted_date)
            date = formatted_date
        except ValueError:
            # print(f"Date format error for row: {row}")
            date = row['Date']

        time = row['Time']

        # Insert data into the table
        insert_query = '''
        INSERT INTO Wifi_data_Transactions (SSID, level, date, Time)
            VALUES (%s, %s, %s, %s)
            '''
        cursor.execute(insert_query, (ssid, level, date, time))

# Commit the changes
connection.commit()
print("Data inserted into `Wifi_data_Transactions`")

# Close the cursor and connection
cursor.close()
connection.close()
print("MySQL connection closed")
