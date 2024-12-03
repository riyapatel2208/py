import re

text = '''Mahatma Gandhi founded Gujarat Vidyapith on October 18, 1920, as a "Rashtriya Vidyapith" or "National University". 
Chancellor: Gandhi served as the university's chancellor, or kulpati, throughout his life. 
Deemed university: Gujarat Vidyapith 7564234123 has been a deemed university since 1963. 
Location: The university is 9494948578 located in Ahmedabad, Gujarat, India. 
Gandhian ethos: The (223) 544 5649 university is a reflection of Gandhian values, with students wearing khadi and inspirational messages from Gandhi on the walls. 
Departments: Some of the 43488 90656  departments at Gujarat Vidyapith include: 
Adhyapak Shiksha Vibhag: This department +8766555234 includes a Hindi teacher training college, a teaching college, and a basic education science institute'''

# regular expressions
pattern1 = r'\d{10}'  # 1234567890
pattern2 = r'\d{5}\s\d{5}'  # 12345 67890
pattern3 = r'\(\d{3}\)\s?\d{3}\D\d{4}'  # (xxx) xxx-xxxx
pattern4 = r'\+\d{10}'  # +1234567890

phone_numbers_10_digits = re.findall(pattern1, text)
phone_numbers_5_5_digits = re.findall(pattern2, text)
phone_numbers_with_parentheses = re.findall(pattern3, text)
phone_numbers_with_plus = re.findall(pattern4, text)

print("PATTERN -- 1234567890 : ",phone_numbers_10_digits)
print()
print("PATTERN -- 12345 67890 : ",phone_numbers_5_5_digits)
print()
print("PATTERN -- (xxx) xxx-xxxx : ",phone_numbers_with_parentheses)
print()
print("PATTERN -- +1234567890 : ",phone_numbers_with_plus)
print()
all_phone_numbers = phone_numbers_10_digits + phone_numbers_5_5_digits + phone_numbers_with_parentheses + phone_numbers_with_plus
print("All Phone Numbers: ",all_phone_numbers)
print()
