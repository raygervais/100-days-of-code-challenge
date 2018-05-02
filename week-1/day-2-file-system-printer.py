import fnmatch as fm
import os

# Printing Function
def file_printer(file, cwd, is_empty, search):
    _, file_type = os.path.splitext(cwd + file)

    if is_empty == True or fm.fnmatch(file, "*{}*".format(search)):
        print("| {:<53} | {:<6} |".format(file, file_type))

def create_table_heading(is_empty_search_criteria):
    print()

    print("{0}{1}{0}".format("|", "-"*64))
    
    if is_empty_search_criteria == True:
        print("{} {:<62} {}".format("|", "Listing Current Working Directory", "|"))
    else:
        print("{} {:<62} {}".format("|", "Listing Matched Search Criteria", "|"))

    print("{0}{1}{0}".format("|", "-"*64))

    print("| File{:<49} | Type{:>2} |".format("", ""))

    print("{0}{1}{0}".format("|", "-"*64))


def main():
    # Get User Search String, if empty we'll list all files in pwd
    criteria = input("Please list the file name or extension: ")

    cwd = os.getcwd()

    # Print CWD for reference
    print("Listing files for {}".format(cwd))
    create_table_heading(len(criteria) == 0)

    for file in os.listdir('.'):
            file_printer(file, cwd, len(criteria) == 0, criteria)

    # Finish Off Table
    print("{0}{1}{0}".format("|", "-"*64))
    print()

main()
