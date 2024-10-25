import csv

# Define the input and output file paths
# input_file_path = 'input_file.csv' # Replace with your input file path
input_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_wifi_data.csv"

# output_file_path = 'unique_capabilities.csv'
output_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/unique_capabilities.csv"
# Use a set to store unique capabilities
unique_capabilities = set()

# Read from the input CSV file
with open(input_file_path, mode='r') as infile:
    reader = csv.DictReader(infile)  # Read the CSV into a dictionary
    for row in reader:
        capabilities = row['Capabilities']  # Access the "Capabilities" field
        # Split the capabilities by '] [' and add to the set
        for capability in capabilities.strip('[]').split(']['):
            unique_capabilities.add(capability)

# Write the unique capabilities to the output CSV file
with open(output_file_path, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Capabilities'])  # Write the header
    for capability in unique_capabilities:
        writer.writerow([capability])  # Write each unique capability
        print(capability)

print(f"CSV file '{output_file_path}' created with unique capabilities.")
