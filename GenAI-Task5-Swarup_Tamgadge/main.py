import Math_utils
import strings_utils

import shop_package


print("----- MATH MODULE -----")

print("Addition:", Math_utils.add(10, 5))
print("Subtraction:", Math_utils.subtract(10, 5))
print("Square:", Math_utils.square(5))


print("\n----- STRING MODULE -----")

text = "python programming"

print("Original String:", text)
print("Capitalized Words:", strings_utils.capitalize_words(text))
print("Reversed String:", strings_utils.reverse_string(text))
print("Number of Vowels:", strings_utils.count_vowels(text))


print("\n----- SHOP PACKAGE -----")

print("Discounted Price:", shop_package.apply_discount(1000, 10))
print("Flat Discount Price:", shop_package.flat_discount(1000))

prices = [100, 200, 300]

total = shop_package.calculate_total(prices)

print("Total:", total)
print("Total After Tax:", shop_package.apply_tax(total))