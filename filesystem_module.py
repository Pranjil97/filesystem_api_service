import os

class FileSystem:

    def __init__(self, directory_path="data") -> None:

        self.data_directory = directory_path
        # self.directory_index = dict()
        # check for data directory
        if os.path.exists(directory_path) == False:
            os.makedirs(directory_path)

    def list_files(self):
        try:    
            return os.listdir(self.data_directory)
        except Exception as e:
            print(f"FileSystemOps :: list_files :: {e}")    
            return []

    def create_file(self, file_name: str, data: any) -> bool:
        try:
            file_path = f"{self.data_directory}/{file_name}"
            if os.path.exists(file_path) == False:
                with open(file_path, "wb") as f:
                    f.write(data)
                return True
            return False
        except Exception as e:
            print(f"FileSystemOps :: create_file :: {file_name} :: {e}")
            return False

    def delete_file(self, file_name) -> bool:
        try:
            file_path = f"{self.data_directory}/{file_name}"
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            return False

        except Exception as e:
            print(f"FileSystemOps :: delete_file :: {file_name} :: {e}")
            return False

    def update_file(self, file_name, data: bytes | str | None) -> bool | None:
        try:
            file_path=f"{self.data_directory}/{file_name}"
            if os.path.exists(file_path) == False:
                return None
            with open(file_path, "wb") as f:
                f.write(data)
            return True
        except Exception as e:
            return False

    def read_file(self, file_name: str) -> bytes | None:
        try:
            file_path = f"{self.data_directory}/{file_name}"
            if os.path.exists(file_path):
                data = None
                with open(file_path, "rb") as f:
                    data = f.read()
                return data
            return None
        except Exception as e:
            print(f"FileSystemOps :: read_file :: {file_name} :: {e}")
            return None
        
        