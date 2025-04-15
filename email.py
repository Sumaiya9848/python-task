def validate_email(email):
    if "@" in email and "." in email:
        if email.endswith('.com') or email.endswith('.in'):
            return True
    return False

email1 = "hello@gmail.com"
email2 = "sumaiyask@gmail.in"
email3 = "skmoin23@gmail.org"

print(validate_email(email1))
print(validate_email(email2))
print(validate_email(email3))
