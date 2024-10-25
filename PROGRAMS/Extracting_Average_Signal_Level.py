import csv

# Define the input and output file paths
input_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_wifi_data.csv"
output_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/average_level.csv"

# Use a dictionary to store SSID and their corresponding levels
ssid_levels = {}

# Read from the input CSV file
with open(input_file_path, mode='r') as infile:
    reader = csv.DictReader(infile)  # Read the CSV into a dictionary
    for row in reader:
        ssid = row['SSID']
        level = int(row['level'])  # Convert level to integer

        # Store levels in a list for each SSID
        if ssid in ssid_levels:
            ssid_levels[ssid].append(level)
        else:
            ssid_levels[ssid] = [level]

    # Calculate the average level for each SSID
    averaged_levels = []
    for ssid, levels in ssid_levels.items():
        average_level = sum(levels) / len(levels)
        averaged_levels.append({'SSID': ssid, 'Average Level': average_level})

    # Write the averaged levels to the output CSV file
    with open(output_file_path, mode='w', newline='') as outfile:

        # Define the output columns
        writer = csv.DictWriter(outfile, fieldnames=['SSID', 'Average Level'])
        writer.writeheader()  # Write the header
        for entry in averaged_levels:
            writer.writerow(entry)  # Write each averaged entry

print(f"CSV file '{output_file_path}' created with average levels.")
