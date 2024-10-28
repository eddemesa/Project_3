import subprocess

# # Run script2.py as a subprocess
# result = subprocess.run(['python', 'script2.py'], capture_output=True, text=True)
#
# # Print the output of script2.py
# print("Output of script2.py:")
# print(result.stdout)
#
# # Print any error messages
# if result.stderr:
#     print("Errors:")
#     print(result.stderr)


class ETL:

    def extract(self):
        # Code to extract data from a source
        result1 = subprocess.run([
            'python',
            'Converting_Multiple_TXT_files_from_multiple_dir_to_CSV.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Multiple_TXT_files_from_multiple_dir_to_CSV.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Extract_Unique_SSID.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Extract_Unique_SSID.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Extracting_Unique_Capabilities.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Extracting_Unique_Capabilities.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Simplify_Unique_SSID_Capabilities.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Simplify_Unique_SSID_Capabilities.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Extracting_Average_Signal_Level.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Extracting_Average_Signal_Level.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Aggregate_Frequency_Usage.py'
            ], capture_output=True, text=True)
        print("Ran succefully: "
              "Aggregate_Frequency_Usage.py")
        # print(result1)


        # Code to transform the extracted data

        result1 = subprocess.run([
            'python',
            'Converting_Wifi_Data_CSV_to_MySQL.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Wifi_Data_CSV_to_MySQL.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Converting_SSID_CSV_to_MySQL_Table.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_SSID_CSV_to_MySQL_Table.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Converting_Average_Signal_Level_to_MySQL.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Average_Signal_Level_to_MySQL.py")
        # print(result1)

        result1 = subprocess.run([
            'python',
            'Converting_Aggregate_Frequency_Usage_to_MySQl.py'
        ], capture_output=True, text=True)
        print("Ran succefully: "
              "Converting_Aggregate_Frequency_Usage_to_MySQl.py")
        # print(result1)



    # def transform(self, data):

    #     # Code to transform the extracted data
    #     pass
    #
    # def load(self, transformed_data):
    #     # Code to load the transformed data into a target
    #     pass


if __name__ == "__main__":
    etl = ETL()
    data = etl.extract()
    # print("Ran succefully: "
    #       "Converting_Multiple_TXT_files_from_multiple_dir_to_CSV.py")
    # return
    # transformed_data = etl.transform(data)
    # etl.load(transformed_data)
