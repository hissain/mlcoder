from mlcoder import file
import argparse
import os
import glob

def main():
    parser = argparse.ArgumentParser(description="MLCoder CLI Utility")

    parser.add_argument("--file", type=str, help="Specify a file name to copy to the working directory")
    parser.add_argument("--search", type=str, help="Search for a file in the example set")
    
    args = parser.parse_args()
    
    if args.file:
        print(f"Processing file: {args.file}")
        caller_directory = os.getcwd()
        file.copy_file_to_working_directory(args.file, caller_dir=caller_directory)

    elif args.search:
        search_pattern = os.path.join(os.path.dirname(__file__), "files", f"*{args.search}*")
        matching_files = glob.glob(search_pattern)

        if matching_files:
            print("Matching files:")
            for match in matching_files:
                print(f"- {os.path.basename(match)}")
        else:
            print("No matching files found.")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
