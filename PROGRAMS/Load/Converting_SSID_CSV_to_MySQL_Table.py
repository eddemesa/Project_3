# pip install mysql-connector-python

import csv
import mysql.connector

# MySQL connection parameters
mysql_host = 'localhost'  # Change if your MySQL server is hosted elsewhere
mysql_database = 'mydb'  # Replace with your database name
mysql_user = 'root'  # Replace with your MySQL username
mysql_password = 'KyleElle$0313'  # Replace with your MySQL password

# CSV file path
csv_file_path = \
    ('/Users/eddemesa/PythonFile/project_3/OUTPUT/'
     'combined_SSID_Capabilities.csv')

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
drop_table_query = 'DROP TABLE IF EXISTS Wifi_SSID_data'
cursor.execute(drop_table_query)
print("Table `Wifi_SSID_data` dropped if it existed")

# Create table SQL statement
create_table_query = '''
    CREATE TABLE IF NOT EXISTS Wifi_SSID_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    SSID VARCHAR(255),
    BSSID VARCHAR(255),
    Capabilities_Code_Combined VARCHAR(15)
    -- Add other columns based on your CSV structure if needed
    )
    '''
# Execute the create table query
cursor.execute(create_table_query)
print("Table `Wifi_SSID_data` created")

# Reading the CSV file and inserting data into the MySQL table
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Prepare the insert statement
        insert_query = '''
        INSERT INTO Wifi_SSID_data (SSID, BSSID, Capabilities_Code_Combined)
        VALUES (%s, %s, %s)
        '''
        # Extract values from the row, make sure to match column names
        values = (row['SSID'], row['BSSID'], row['Capabilities_Code_Combined'])

        # Execute the insert statement
        cursor.execute(insert_query, values)

# Commit the transaction
connection.commit()
print(f"Data from {csv_file_path} has been "
      f"successfully inserted into the `Wifi_SSID_data` table.")

# Close the cursor and connection
cursor.close()
connection.close()
