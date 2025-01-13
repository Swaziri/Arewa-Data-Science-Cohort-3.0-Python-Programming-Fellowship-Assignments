import re
filename =  r'C:\Users\Dell\Desktop\Arewa Data Science Fellowship\data\email_exchanges.txt'
def extract_email_addresses(filename):
    email_addresses = []
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            emails = re.findall(email_pattern, line)
            email_addresses.extend(emails)
    return list(set(email_addresses))
emails = extract_email_addresses('./data/email_exchanges.txt')
print(emails)
