
import pandas as pd
import json
import os
from datetime import datetime
# import pytz
# import re


def extract_data_from_txt_files(input_directory, output_file):
    # Initialize a list to hold the records
    records = []

    # Walk through the directory and subdirectories
    for dirpath, _, filenames in os.walk(input_directory):
        print('Processing' + dirpath)

        for filename in filenames:
            if filename.endswith('.txt'):
                # Construct the full file path
                file_path = os.path.join(
                    dirpath,
                    filename
                )
                # Read the contents of the file
                try:
                    with (open(
                            file_path,
                            'r',
                            encoding='ISO-8859-1',
                            errors='replace'
                    ) as file):
                        for line in file:
                            # Load the JSON data
                            try:
                                # Ensure json_data is a dictionary
                                json_data = json.loads(line)
                                if isinstance(json_data,
                                              dict) and \
                                        "WiFi" in json_data:
                                    wifi_info = json_data["WiFi"]
                                    # Initialize time_str before use
                                    # Get and strip whitespace
                                    time_str = wifi_info.get('time',
                                                             '').strip()

                                    # Check if time_str is valid and not empty
                                    if time_str:
                                        # Attempt to parse the time string
                                        try:  # Time string is valid
                                            time_str = wifi_info.get('time',
                                                                     '')
                                            # Extracting the Date part
                                            str1 = time_str.split()
                                            date_string = (str1[1] +
                                                           " " +
                                                           str1[2] +
                                                           " " +
                                                           str1[3])
                                            try:
                                                date_object = (
                                                    datetime.strptime(
                                                        date_string,
                                                        "%B %Ω %Y"
                                                    ))
                                                formatted_date = (
                                                    date_object.strftime(
                                                        "%m/%d/%Y"))
                                                # Format date to US format
                                            except ValueError as ve:
                                                print(
                                                    f"Invalid date format:"
                                                    f" {date_string} "
                                                    f"in file: {filename}. "
                                                    f"Error: {ve}")
                                                continue

                                            # Original time string
                                            time_string = (
                                                    str1[4] +
                                                    " " +
                                                    str1[5]
                                            )

                                            # Parse the time string
                                            # into a datetime object
                                            time_object = (
                                                datetime.strptime(
                                                    time_string,
                                                    "%I:%M:%S %p")
                                            )

                                            # Output the result
                                            time_data = time_object.time()

                                            record = {
                                                "Directory name":
                                                    dirpath,
                                                "File name":
                                                    filename,
                                                # Placeholder for
                                                # Application data
                                                "Application":
                                                    None,
                                                "SSID":
                                                    wifi_info.get("SSID"),
                                                "BSSID":
                                                    wifi_info.get("BSSID"),
                                                "Capabilities":
                                                    wifi_info.get(
                                                        "capabilities"),
                                                "level":
                                                    wifi_info.get("level"),
                                                "frequency":
                                                    wifi_info.get(
                                                        "frequency"),
                                                "Date":
                                                    formatted_date,
                                                "Time":
                                                    time_data
                                            }
                                            records.append(record)
                                            print(record)
                                        except json.JSONDecodeError as err1:
                                            print(f"Invalid time format: "
                                                  f"{time_str} "
                                                  f"in file: {filename}",
                                                  f"Error: {err1}")
                                            continue

                            except json.JSONDecodeError as err2:
                                print(f"Error encountered: "
                                      f"{err2}")
                                continue
                                # Skip lines that cannot
                                # be parsed as JSON
                            finally:
                                pass

                except json.JSONDecodeError as err3:
                    print(f"Error encountered: {err3}")
                    continue
                    # Skip lines that
                    # cannot be parsed as JSON
                finally:
                    pass

    # Create a DataFrame from the records
    df = pd.DataFrame(records)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    print(f"Data has been extracted and saved to: "
          f"{output_file}")


# Main function
def main():
    # Directory containing the text files
    input_directory = \
        "/Users/eddemesa/PythonFile/project_3/INPUT/UbiqLog4UCI"

    # Output CSV file
    output_file = \
        "/Users/eddemesa/PythonFile/project_3/OUTPUT/combined_wifi_data.csv"

    # Extract data from text files and save to CSV
    extract_data_from_txt_files(input_directory, output_file)


if __name__ == "__main__":
    main()
