import csv
from collections import defaultdict

# Define the input and output file paths
input_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_wifi_data.csv"
output_file_path = \
    "/Users/eddemesa/PythonFile/project_3/OUTPUT/Aggregate_Frequency_Usage.csv"

# Use a dictionary to store the
# count of SSIDs for each frequency
frequency_count = defaultdict(int)

# Read from the input CSV file
with open(input_file_path, mode='r') as infile:
    # Read the CSV into a dictionary
    reader = csv.DictReader(infile)
    for row in reader:
        # Access the frequency field
        frequency = row['frequency']
        # Increment the count for that frequency
        frequency_count[frequency] += 1

        # Prepare the data for writing to the output CSV file
        aggregated_data = [{'Frequency': freq,
                           'Total_SSID': count} for freq,
                           count in frequency_count.items()]

    # Write the aggregated frequency usage to the output CSV file
    with open(output_file_path, mode='w', newline='') as outfile:
        # Define the output columns
        writer = csv.DictWriter(outfile, fieldnames=[
                                'Frequency',
                                'Total_SSID']
                                )
        # Write the header
        writer.writeheader()
        for entry in aggregated_data:
            # Write each aggregated entry
            writer.writerow(entry)

print(f"CSV file '{output_file_path}' "
      f"created with Aggregate Frequency Usage.")
