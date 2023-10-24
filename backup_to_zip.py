import zipfile
import os

def backup_to_zip(folder, zip_filename):
    # Ensure the folder exists
    if not os.path.exists(folder):
        print(f"The specified folder '{folder}' does not exist.")
        return

    # Create a new ZIP file or overwrite an existing one
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
        for foldername, subfolders, filenames in os.walk(folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                # Create relative path by removing the common prefix (the folder to be backed up)
                relative_path = os.path.relpath(file_path, folder)
                backup_zip.write(file_path, relative_path)

    print(f'Backup of folder "{folder}" created as "{zip_filename}".')

if __name__ == "__main__":
    folder_to_backup = input("Enter the folder path to back up: ")
    zip_filename = input("Enter the zip file name for the backup: ")

    if not zip_filename.endswith('.zip'):
        zip_filename += '.zip'

    backup_to_zip(folder_to_backup, zip_filename)
