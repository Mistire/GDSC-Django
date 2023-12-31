# Create a Python script that identifies and collects files (both created and modified) in the last 24 hours from the current directory. Update these files in some way and move them to a folder named "last_24hours."

## Requirements

### Listing Files

- Use the os module to list all files in the current directory.

### Identification of Files

- Implement a function to determine whether a file has been created or modified in the last 24 hours.
- Consider both the modification time (st_mtime) and creation time (st_ctime) of the file.

### Update Files

- Create a function to update the identified files. For example, append a timestamp to the content of each file.

### Create "last_24hours" Folder

- Check if a folder named "last_24hours" exists. If not, create it using the os module.

### Move Files

- Move the identified and updated files to the "last_24hours" folder using different method
- Combine the functions to achieve the main objective.

Feel free to seek clarification on any part of the task. The primary goal is to enhance your understanding of file handling, time-based operations, and module usage in Python.
