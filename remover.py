import os
from typing import List, Dict

def get_file_info_list(directory: str) -> List[Dict[str, str]]:
    """
    Get a list of file information dictionaries for all files in the specified directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing file information.
    """
    file_info_list = []
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_info = {
                'name': filename,
                'path': file_path,
                'size': str(os.path.getsize(file_path)),
                'modified_time': str(os.path.getmtime(file_path))
            }
            file_info_list.append(file_info)
    
    return file_info_list

def scan_subfolders(directory: str) -> List[Dict[str, str]]:
    """
    Scan all subfolders in the specified directory and add them, along with their file information, to a list.
    
    Args:
        directory (str): The path to the directory.
        
    Returns:
        List[Dict[str, str]]: A list of dictionaries containing file information for all files in the directory and its subfolders.
    """
    file_info_list = get_file_info_list(directory)
    
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            subfolder_path = os.path.join(root, dir_name)
            subfolder_file_info_list = get_file_info_list(subfolder_path)
            file_info_list.extend(subfolder_file_info_list)
    
    return file_info_list

def remove_specified_filetype(directory: str, file_extension: str) -> None:
    """
    Remove all files of the specified file type from the given directory and its subfolders.

    Args:
        directory (str): The path to the directory.
        file_extension (str): The file extension to remove (e.g., '.txt').
    """
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(file_extension):
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"Removed: {file_path}")
                except Exception as e:
                    print(f"Error removing {file_path}: {e}")

if __name__ == "__main__":
    
    directory = input("Enter the directory path: ")
    file_extension = input("Enter the file extension to remove (e.g., .txt): ")
    
    if os.path.isdir(directory):
        file_info_list = scan_subfolders(directory)
        for file_info in file_info_list:
            print(file_info)
        remove_specified_filetype(directory, file_extension)
    else:
        print("The specified path is not a valid directory.")