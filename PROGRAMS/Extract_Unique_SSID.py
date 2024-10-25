import pandas as pd


def extract_unique_ssid_data(input_file_path, output_file_path):
    # Read the CSV file into a DataFrame
    try:
        data = pd.read_csv(input_file_path)
        print(f"Successfully read CSV file: {input_file_path}")
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return

    # Check if required columns exist
    required_columns = ['SSID', 'BSSID', 'Capabilities']
    for column in required_columns:
        if column not in data.columns:
            print(f"Error: '{column}' column not found in the CSV file.")
            return

    # Drop duplicates based on 'SSID' and keep the first occurrence
    unique_data = data.drop_duplicates(subset='SSID')[required_columns]

    # Save the unique data to a new CSV file
    unique_data.to_csv(output_file_path, index=False)
    print(
        f"Unique SSIDs along with BSSID, and Capabilities, "
        f"have been extracted and saved to: {output_file_path}")


# Main function
def main():
    # Path to the CSV file
    input_file_path = \
        '/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_wifi_data.csv'

    # Path for the output CSV file
    output_file_path = \
        '/Users/eddemesa/PythonFile/project_3/OUTPUT/filtered_ssid_data.csv'

    # Extract unique SSID data
    extract_unique_ssid_data(
        input_file_path,
        output_file_path
    )


if __name__ == "__main__":
    main()
