import json
import zipfile

user_file = "users.json"
computer_file = "computers.json"


def open_zip(file_path):
    with zipfile.ZipFile(file_path) as zip_file:
        data = {}
        filenames_to_search = [user_file, computer_file]
        for file in zip_file.namelist():
            for search in filenames_to_search:
                if file.endswith(search):
                    with zip_file.open(file) as zipped_file:
                        file_data = zipped_file.read()
                        json_data = json.loads(file_data)
                        data[search] = json_data
        return data
