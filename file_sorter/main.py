import os
import shutil


class File_Sorter:
    def __init__(self):
        self.main()

    def create_folder(self, path: str, extension: str) -> str:
        folder_name: str = extension[1:]
        folder_path: str = os.path.join(path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path

    def sort_files(self, source_path: str):
        for root_dir, sub_dir, filenames in os.walk(source_path):
            for filename in filenames:
                file_path: str = os.path.join(root_dir, filename)
                extension: str = os.path.splitext(filename)[1]

                if extension:
                    target_folder: str = self.create_folder(source_path, extension)
                    target_path: str = os.path.join(target_folder, filename)

                    shutil.move(file_path, target_path)

    def remove_empty_folders(self, source_path: str):
        for root_dir, sub_dir, filenames in os.walk(source_path, topdown=False):
            for current_dir in sub_dir:
                folder_path: str = os.path.join(root_dir, current_dir)

                if not os.listdir(folder_path):
                    os.rmdir(folder_path)

    def main(self):
        user_input: str = input("Please provide a file path to sort: ")

        if os.path.exists(path=user_input):
            self.sort_files(user_input)
            self.remove_empty_folders(user_input)

sorter = File_Sorter()