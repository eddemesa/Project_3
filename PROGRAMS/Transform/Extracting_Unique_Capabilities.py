import csv

# Define the input and output file paths
input_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_wifi_data.csv"
output_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/unique_capabilities.csv"

# Use a set to store unique capabilities
unique_capabilities = set()

# Read from the input CSV file
with open(input_file_path, mode='r') as infile:
    reader = csv.DictReader(infile)  # Read the CSV into a dictionary
    for row in reader:
        # Access the "Capabilities" field
        capabilities = row['Capabilities']
        # Split the capabilities by "[]" and add to the set
        for capability in capabilities.strip('[]').split(']['):
            unique_capabilities.add(capability)

# Write the unique capabilities and their
# auto-incrementing codes to the output CSV file
with open(output_file_path, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    # Write the header
    writer.writerow(['Capabilities_Code', 'Capabilities'])

    # Initialize the counter for capabilities_code
    capabilities_code = 1
    for capability in unique_capabilities:
        # Write each unique capability with its code
        writer.writerow([capabilities_code, capability])
        # Print the capability with its code
        print(f"{capabilities_code}: {capability}")
        # Increment the code for the next capability
        capabilities_code += 1

print(f"CSV file '{output_file_path}' "
      f"created with unique capabilities and their codes.")
