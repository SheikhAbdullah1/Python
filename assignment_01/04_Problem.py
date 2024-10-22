import os
# Select the directory path which ant to folder list
directory_path = '/Portfolio'

# OS Model list the directory of your disk/folder structure
contents = os.listdir(directory_path)

# Print the folder and file with the elp of for in loop
for item in contents:
    print(item)
