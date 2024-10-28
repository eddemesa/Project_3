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
     'Aggregate_Frequency_Usage.csv')

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
drop_table_query = 'DROP TABLE IF EXISTS Aggregate_Frequency_Usage'
cursor.execute(drop_table_query)
print("Table Aggregate_Frequency_Usage dropped if it existed")

# Create table SQL statement
create_table_query = '''
    CREATE TABLE IF NOT EXISTS Aggregate_Frequency_Usage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Frequency VARCHAR(255),
    Total_SSID Numeric(10)
    -- Add other columns based on your CSV structure if needed
    )
    '''
# Execute the create table query
cursor.execute(create_table_query)
print("Table Aggregate_Frequency_Usage created")

# Reading the CSV file and inserting data into the MySQL table
with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        # Prepare the insert statement
        insert_query = '''
        INSERT INTO Aggregate_Frequency_Usage (Frequency, Total_SSID)
        VALUES (%s, %s)
        '''
        # Extract values from the row, make sure to match column names
        values = (row['Frequency'], row['Total_SSID'])

        # Execute the insert statement
        cursor.execute(insert_query, values)

# Commit the transaction
connection.commit()
print(f"Data from {csv_file_path} has been "
      f"successfully inserted into the Aggregate_Frequency_Usage table.")

# Close the cursor and connection
cursor.close()
connection.close()
