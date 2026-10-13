file_name = input("Enter the file name: ")

try:
    with open(file_name, "r") as file:

        lines = file.readlines()

        print("First 3 lines:")

        for line in lines[:3]:
            print(line, end="")

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

finally:
    print("File operation attempted.")