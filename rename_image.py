import os

directory = "C:\\Users\\Zebus\\Desktop\\rice\\Rice_Image_Dataset"

# Loop through the folders and the images in the folders to rename them
for dirpath, dirnames, filenames in os.walk(directory):
    # Get the name of the current folder
    folder_name = os.path.basename(dirpath)
    for i, filename in enumerate(filenames):
        # Check if the file is an image (optional)
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Create a new name for the file
            new_name = f'{folder_name}_{i+1}{os.path.splitext(filename)[1]}'
            
            # Define the full path for the old and new file names
            old_file = os.path.join(dirpath, filename)
            new_file = os.path.join(dirpath, new_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

print("Renaming completed.")
