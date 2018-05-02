import fnmatch as fm
import os

# Printing Function
def file_printer(file, cwd, is_empty):
    _, file_type = os.path.splitext(cwd + file)
   
    if is_empty == True:
        print("File:{:<36} Type: {:<2}".format(file, file_type))
    else:
        print("Matched File:{:<36} Type: {:<2}".format(file, file_type))

# Get User Search String, if empty we'll list all files in pwd
critera = input("Please list the file name or extension: ")

cwd = os.getcwd()

# Print CWD for reference
print("Listing files for {}".format(cwd))

for file in os.listdir('.'):
    if len(critera) != 0 and fm.fnmatch(file, '*{}*'.format(critera)):
        file_printer(file, cwd, False)
    elif len(critera) == 0:
        file_printer(file, cwd, True)
