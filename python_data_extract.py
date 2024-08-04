# Import the operating system
import os

# Define the directory to be scanned
current_directory = os.getcwd()

# Create the empty list to store file information
Files = []

# Iterate over all items in the directory
for file in os.listdir(current_directory):
    # Provide the full file path
    file_path = os.path.join(current_directory, file)
     # Verify that it is a file
    if os.path.isfile(file_path):
       # Get the file size
        file_size = os.path.getsize(file_path)
         # Create a dictionary with both the file and the size
        Data = {'path': file_path, 'size': file_size}
         # Append the dictionary to the list
        Files.append(Data)


# Print the file paths and sizes
for file_info in Files:
    print(f"File Path: {file_info['path']} | Size: {file_info['size']} bytes")
