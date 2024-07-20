import os
import shutil

def organize_files(directory):
    # Change the current working directory to the specified directory
    os.chdir(directory)

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(filename):
            continue
        
        # Get the file extension
        file_extension = filename.split('.')[-1]
        
        # Define the new directory name based on the file extension
        new_directory = file_extension.upper() + "Files"

        # Create the new directory if it does not exist
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        
        # Move the file to the new directory
        shutil.move(filename, os.path.join(new_directory, filename))
        

if __name__ == "__main__":
    # Specify the directory you want to organize
    directory_to_organize = input("Enter the path to the directory you want to organize: ")
    organize_files(directory_to_organize)
    print("Files have been organized.")
