import re
# The 1 example

# email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
#
# email_check_pattern= re.compile(email_regexp)
#
# print(email_check_pattern.fullmatch('neftianik@inbox.ru')) # match='neftianik@inbox.ru'

# create function 2 example

def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(email) else "not valid"
    return (email,validation_result)


# Valid
print(check_email('neftianik@inbox.ru')) # ('neftianik@inbox.ru', 'valid')

# Invalid
print(check_email('neftianikinbox.ru')) # ('neftianikinbox.ru', 'not valid')
