import re

text = """
Jane Smith (jane.smith@example.com) ordered 2 items worth $59.99 on 2024-10-16. 
Her contact number is (555) 987-6543. 
John Doe (john.doe123@example.org) purchased a laptop on 2024-10-10 for $1200. His phone number is 555-321-7654. 
Alice Cooper (alice_cooper@company.co) is our lead developer. Her phone number is 555 987 6543.
Mary Ann (mary.ann@workplace.org) signed up for the newsletter. Her contact is (333) 123-5678, located in Suite 500, Tech Park.
Also, her order number is 1234567890 (valid phone number format).
"""

# Regex for extracting email addresses
email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_regex, text)
print("Emails found:", emails)

# Regex for extracting phone numbers
# Updated to also match plain 10-digit numbers like 1234567890
phone_regex = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}|\d{10}'
phones = re.findall(phone_regex, text)
print("Phone numbers found:", phones)

# Additional validation: Extracting valid emails and phone numbers with more constraints

# Validating if email address ends with a valid domain (e.g., .com, .org, .net, etc.)
valid_email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|org|net|edu|gov|co|io|tech)$'
valid_emails = [email for email in emails if re.match(valid_email_regex, email)]
print("Valid emails:", valid_emails)

# Validating phone numbers: Ensuring the area code is 3 digits, the central office code is 3 digits, and the line number is 4 digits.
valid_phone_regex = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$|\d{10}$'
valid_phones = [phone for phone in phones if re.match(valid_phone_regex, phone)]
print("Valid phone numbers:", valid_phones)
