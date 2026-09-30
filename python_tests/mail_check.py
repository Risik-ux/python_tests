import re
import sys

def finalize(message, code=1):
    print(message, file=sys.stderr)
    sys.exit(code)

def email_verify(email):
    email = email.strip().lower()
    if not re.match(r"^[^\s]+@[^\s]+\.[^\s]{2,}$", email):
        finalize(f"Invalid structure email (example: <name@mail.com>): {email}")
    if len(email) < 6:
        finalize(f"email too short, less that 5 letter: {email}")
    if len(email) > 254:
        finalize(f"email too long: {email}")
    if email.count("@") != 1:
        finalize(f"wrong count @ symbols: {email}")
    if ".." in email:
        finalize(f"too many dots in a row in the email: {email}")
    email_local_part, email_domain_part = email.split("@")
    if any(p.startswith(".") or p.endswith(".") 
           for p in (email_local_part, email_domain_part)):
        finalize(f"Dot state in wrong position: {email}")
    if "." not in email_domain_part:
        finalize(f"Domain part not contained dot: {email}")
    return email

email = email_verify(input("Введите адрес почты: "))
print(email)
