import os
import sys

def add_txt_extension(directory):
    """
    Recursively goes through the given directory and all its subdirectories,
    and adds a .txt extension to all files that don't already have it.
    """
    # Check if directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return False
        
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            
            # Check if the file already has a .txt extension
            if not file_path.endswith('.txt'):
                # Create the new file name with .txt extension
                new_file_path = file_path + '.txt'
                
                # Rename the file
                try:
                    os.rename(file_path, new_file_path)
                    print(f"Renamed: {file_path} -> {new_file_path}")
                except Exception as e:
                    print(f"Error renaming {file_path}: {e}")
    
    return True

if __name__ == "__main__":
    # Check if directory path is provided as command line argument
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        # Ask user for directory path
        target_directory = input("Enter the path of the folder to process (or press Enter for current directory): ")
        
        # If user didn't enter anything, use current directory
        if not target_directory:
            target_directory = os.getcwd()
    
    # Convert to absolute path
    target_directory = os.path.abspath(target_directory)
    
    # Confirm with the user before proceeding
    print(f"This will add .txt extension to all files in '{target_directory}' and its subdirectories.")
    confirmation = input("Do you want to proceed? (y/n): ")
    
    if confirmation.lower() == 'y':
        if add_txt_extension(target_directory):
            print("File renaming completed.")
    else:
        print("Operation cancelled.")