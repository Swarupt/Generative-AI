# Using read()

with open("sales_data.txt", "r") as file:

    content = file.read()

print("Using read():")
print(content)


# Using readline()

with open("sales_data.txt", "r") as file:

    first_line = file.readline()

print("Using readline():")
print(first_line)


# Using readlines()

with open("sales_data.txt", "r") as file:

    lines = file.readlines()

sales = []

for line in lines:
    sales.append(int(line.strip()))

print("Using readlines():")
print(sales)