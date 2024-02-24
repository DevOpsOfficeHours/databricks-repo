# Databricks notebook source
# Import the required libraries
import os
import shutil

# Specify the file paths
source_file_path = "path/to/source_file.txt"
destination_directory = "path/to/destination_directory"

# Check if the source file exists
if os.path.exists(source_file_path):
    # Check if the destination directory exists, if not create it
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    
    # Generate a unique filename for the destination file
    destination_file_path = os.path.join(destination_directory, "destination_file.txt")
    
    # Copy the source file to the destination directory
    shutil.copy2(source_file_path, destination_file_path)
    
    # Rename the copied file to include a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    new_destination_file_path = os.path.join(destination_directory, f"destination_file_{timestamp}.txt")
    os.rename(destination_file_path, new_destination_file_path)
else:
    print("Source file does not exist.")
