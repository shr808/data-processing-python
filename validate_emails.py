"""
Validate Email Addresses

Performs basic email format validation.
"""

emails = [
    "john.doe@company.com",
    "mary.smith@email.org",
    "invalid-email",
    "user@website",
    "test@test.co.uk",
    "@nodomain.com",
    "spaces not allowed@email.com"
]

def is_valid_email(email: str) -> bool:
    """
    Basic email validation rules:
    - One @ symbol
    - Non-empty local and domain parts
    - Domain contains a dot
    - No spaces
    """
    if " " in email or "@" not in email:
        return False

    local, domain = email.split("@", 1)
    return bool(local) and "." in domain

print("VALIDATING EMAIL ADDRESSES")
print("-" * 30)

valid_count = 0
for email in emails:
    is_valid = is_valid_email(email)
    status = "VALID" if is_valid else "INVALID"
    print(f"{email:32} -> {status}")
    valid_count += int(is_valid)

print(f"\nValid emails: {valid_count}/{len(emails)}")
