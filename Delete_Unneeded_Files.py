import os

def find_large_files(starting_folder, size_limit):
    for foldername, subfolders, filenames in os.walk(starting_folder):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_size = os.path.getsize(file_path)
            if file_size > size_limit:
                print(f"Large file found: {file_path} ({file_size} bytes)")

if __name__ == "__main__":
    starting_folder = input("Enter the folder path to start the search: ")
    size_limit = 100 * 1024 * 1024  # 100MB in bytes

    if os.path.exists(starting_folder) and os.path.isdir(starting_folder):
        find_large_files(starting_folder, size_limit)
    else:
        print("Invalid folder path. Please provide a valid directory path.")
