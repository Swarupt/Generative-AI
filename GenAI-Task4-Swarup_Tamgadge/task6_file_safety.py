import os

file_name = input("Enter the file name: ")

if os.path.exists(file_name):

    with open(file_name, "r") as file:

        content = file.read()

    print("File contents:")
    print(content)

else:

    print("File not found. Please check the filename.")