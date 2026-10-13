def capitalize_words(text):
    return text.title()


def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    count = 0

    for character in text:

        if character.lower() in "aeiou":
            count = count + 1

    return count