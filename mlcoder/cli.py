import argparse
import os
import importlib.resources
from mlcoder import file

def get_package_data_directory():
    """Get the absolute path to the package's 'files' directory."""
    return os.path.join(importlib.resources.files("mlcoder"), "files")

def main():
    parser = argparse.ArgumentParser(description="MLCoder CLI Utility")

    # Define two positional arguments (exactly one required)
    parser.add_argument("command", choices=["search", "copy"], help="Command to execute: 'search' or 'copy'")
    parser.add_argument("argument", type=str, help="File name for 'copy' or search term for 'search'")

    args = parser.parse_args()

    files_dir = get_package_data_directory()

    # Handle 'copy' command
    if args.command == "copy":
        print(f"Copying file: {args.argument}")
        caller_directory = os.getcwd()
        file.copy_file_to_working_directory(args.argument, caller_dir=caller_directory, source_dir=files_dir)

    # Handle 'search' command
    elif args.command == "search":
        search_term = args.argument
        matching_files = []

        for root, dirs, files in os.walk(files_dir):
            for name in files:
                if search_term in name:
                    full_path = os.path.join(root, name)
                    relative_path = os.path.relpath(full_path, files_dir)
                    matching_files.append(relative_path)

        if matching_files:
            print("Matching files:")
            for match in matching_files:
                print(f"- {match}")
        else:
            print("No matching files found.")

if __name__ == "__main__":
    main()