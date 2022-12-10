import os


def files_path(path):
    csv_file_path = ""
    print("before list dir", path)
    for file in os.listdir(path):
        if file == "examples.csv":
            csv_file_path = file
            print(path)
            return f"{path}/{file}"
    if csv_file_path == "":
        with open(f"{path}/examples.csv", 'w') as file:
            csv_file_path = f"{path}/examples.csv"
            file.close()
        return csv_file_path