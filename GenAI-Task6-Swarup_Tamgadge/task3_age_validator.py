def check_age(age):

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    return age


try:
    age = int(input("Enter your age: "))

    check_age(age)

    print("Valid age:", age)

except ValueError as error:
    print(error)