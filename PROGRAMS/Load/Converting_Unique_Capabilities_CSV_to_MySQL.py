import csv
import mysql.connector

# MySQL connection parameters
mysql_host = 'localhost'  # Change if your MySQL server is hosted elsewhere
mysql_database = 'mydb'  # Replace with your database name
mysql_user = 'root'  # Replace with your MySQL username
mysql_password = 'KyleElle$0313'  # Replace with your MySQL password

# CSV file path
csv_file_path = \
    '/Users/eddemesa/PythonFile/project_3/OUTPUT/unique_capabilities.csv'

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
drop_table_query = 'DROP TABLE IF EXISTS Unique_Capabilities'
cursor.execute(drop_table_query)
print("Table `Unique_Capabilities` dropped if it existed")

# Create a new table
create_table_query = '''
    CREATE TABLE Unique_Capabilities (
    Capabilities_Code INT AUTO_INCREMENT PRIMARY KEY,
    Capabilities VARCHAR(255) NOT NULL
    )
    '''
cursor.execute(create_table_query)
print("Table `Unique_Capabilities` created")

# Read data from the CSV file and insert it into the MySQL table
with open(csv_file_path, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)  # Read the CSV into a dictionary
    for row in reader:
        capabilities = row['Capabilities']  # Extract the capabilities field

        # Insert the data into the table
        insert_query = '''
            INSERT INTO Unique_Capabilities (Capabilities)
            VALUES (%s)
            '''
        cursor.execute(insert_query, (capabilities,))

# Commit the changes
connection.commit()
print("Data inserted into `Unique_Capabilities` table")

# Close the cursor and connection
cursor.close()
connection.close()
print("MySQL connection closed")
