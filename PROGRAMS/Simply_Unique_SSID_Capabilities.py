"""
To create a Python script that combines data from
unique_ssid_data.csv and unique_capabilities.csv
into a new CSV file, we will follow these steps:
1. Read the data from both CSV files.
2. Extract the capabilities from unique_capabilities.csv.
3. Map the capabilities found in unique_ssid_data.csv
   to their corresponding codes.
4. Create a new CSV file that includes the SSID, BSSID,
combined Capabilities_Code, and Frequency.
"""

import csv


def read_capabilities(filename):
    capabilities_map = {}
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create a mapping from capabilities to their codes
            capabilities_map[row['Capabilities']] = row['Capalilities_code']
    return capabilities_map


def process_ssid_data(ssid_file, capabilities_map, output_file):
    with open(ssid_file, mode='r', newline='') as ssid_csv:
        ssid_reader = csv.DictReader(ssid_csv)
        with open(output_file, mode='w', newline='') as output_csv:
            fieldnames = ['SSID', 'BSSID', 'Capabilities_Code']
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            writer.writeheader()

            for row in ssid_reader:
                # Extract capabilities from the SSID data
                capabilities = row["Capabilities"].strip('[]').split('][')
                # Map the capabilities to their codes
                capabilities_codes = [capabilities_map.get(capability, "") for capability in capabilities]
                # Join the codes with a comma
                capabilities_code_combined = ','.join(filter(None, capabilities_codes))

                # Write the new row to the output CSV
                writer.writerow({
                    'SSID': row["SSID"],
                    'BSSID': row["BSSID"],
                    'Capabilities_Code': capabilities_code_combined
                })


if __name__ == "__main__":
    capabilities_file = \
        '/Users/eddemesa/PythonFile/project_3/OUTPUT/unique_capabilities.csv'
    ssid_data_file = \
        '/Users/eddemesa/PythonFile/project_3/OUTPUT/unique_ssid_data.csv'
    output_csv_file = \
        '/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_SSID_Capabilities.csv'

    # Read capabilities and process SSID data
    capabilities = read_capabilities(capabilities_file)
    process_ssid_data(ssid_data_file, capabilities, output_csv_file)
