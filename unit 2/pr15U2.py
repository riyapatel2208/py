import re

def find_emails(paragraph):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, paragraph)
    return emails

paragraph = """
    Here are some email addresses: john.doe@example.com, jane_doe123@domain.co, 
    test.email+alex@subdomain.example.com, invalid_email@domain@com, user@com, 
    another_valid_email@another-domain.org. 
"""

emails = find_emails(paragraph)
print("Found emails:", emails)
