import subprocess


class ETL:

    @staticmethod
    def extract():
        # Code to extract data from a source
        result1 = subprocess.run([
            'python',
            'Converting_Multiple_TXT_files_from_multiple_dir_to_CSV.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Multiple_TXT_files_from_multiple_dir_to_CSV.py")
        print(result1)

    # Code to transform the extracted data
    @staticmethod
    def transform():

        result1 = subprocess.run([
            'python',
            'Extract_Unique_SSID.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Extract_Unique_SSID.py")
        print(result1)

        result1 = subprocess.run([
            'python',
            'Extracting_Unique_Capabilities.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Extracting_Unique_Capabilities.py")
        print(result1)

        result1 = subprocess.run([
            'python',
            'Simplify_Unique_SSID_Capabilities.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Simplify_Unique_SSID_Capabilities.py")
        print(result1)

        result1 = subprocess.run([
            'python',
            'Extracting_Average_Signal_Level.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Extracting_Average_Signal_Level.py")
        print(result1)

        result1 = subprocess.run([
            'python',
            'Aggregate_Frequency_Usage.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Aggregate_Frequency_Usage.py")
        print(result1)

    @staticmethod
    def load():
        result1 = subprocess.run([
            'python',
            'Converting_Wifi_Data_CSV_to_MySQL.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Wifi_Data_CSV_to_MySQL.py")
        print(result1)

        result1 = subprocess.run([
            'python',
            'Converting_SSID_CSV_to_MySQL_Table.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_SSID_CSV_to_MySQL_Table.py")
        print(result1)

        result1 = subprocess.run([
            'python',
            'Converting_Average_Signal_Level_to_MySQL.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Average_Signal_Level_to_MySQL.py")
        print(result1)

        result1 = subprocess.run([
            'python',
            'Converting_Aggregate_Frequency_Usage_to_MySQl.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Aggregate_Frequency_Usage_to_MySQl.py")
        print(result1)


if __name__ == "__main__":
    etl = ETL()
    print("Processing Extraction......")
    etl.extract()
    print("Processing Transformation......")
    etl.transform()
    print("Processing Load - Conversion to MySQL Database ......")
    etl.load()
