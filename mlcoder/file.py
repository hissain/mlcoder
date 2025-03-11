# mlcoder/file.py

import os
import shutil

def copy_file_to_working_directory(filename, filedir='files'):
    """
    Copies a file from the specified folder to the directory of the caller script.

    Parameters:
    filename (str): The name of the file to copy.
    filedir (str): The directory where the source file is located.
    """
    source_path = os.path.join(os.path.dirname(__file__), filedir, filename)
    print(source_path)

    # Get the directory of the caller script
    caller_directory = os.path.dirname(os.path.abspath(__file__))
    destination_path = os.path.join(caller_directory, filename)
    print(destination_path)
    
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"The file {filename} does not exist in the ./{filedir} directory.")
    
    shutil.copy(source_path, destination_path)
    print(f"Copied {filename} to {caller_directory}")

# Example usage
if __name__ == "__main__":
    try:
        copy_file_to_working_directory('pretty_print.py')
    except FileNotFoundError as e:
        print(e)