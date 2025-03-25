# my_package/string_ops.py

def capitalize_string(s):
    return s.capitalize()

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum([1 for char in s if char.lower() in 'aeiou'])

def is_palindrome(s):
    return s == s[::-1]
