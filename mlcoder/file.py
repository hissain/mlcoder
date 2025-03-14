# mlcoder/file.py

import os
import shutil
import inspect

def copy_file_to_working_directory(filename, caller_dir=None, source_dir='files'):
    source_path = os.path.join(os.path.dirname(__file__), source_dir, filename)

    if caller_dir:
        destination_path = os.path.join(caller_dir, filename)
    else:
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        caller_directory = os.path.dirname(os.path.abspath(caller_file))
        destination_path = os.path.join(caller_directory, filename)
    
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"The file {filename} does not exist in the ./{source_dir} directory.")
    
    shutil.copy(source_path, destination_path)
    print(f"Copied {filename} to {destination_path}")

# Example usage
if __name__ == "__main__":
    try:
        copy_file_to_working_directory('pretty_print.py')
    except FileNotFoundError as e:
        print(e)