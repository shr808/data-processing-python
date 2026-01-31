"""
Format Phone Numbers

Standardizes phone numbers into a consistent format.
"""

import re

phones = [
    "555-123-4567",
    "(555) 987 6543",
    "555.123.4567",
    "5551234567",
    "1-555-123-4567"
]

def format_phone(phone: str) -> str:
    """
    Convert phone numbers to (XXX) XXX-XXXX format.
    Keeps last 10 digits when country code exists.
    """
    digits = re.sub(r"\D", "", phone)

    if len(digits) < 10:
        return phone

    digits = digits[-10:]
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

print("FORMATTING PHONE NUMBERS")
print("-" * 25)

for phone in phones:
    print(f"{phone:20} -> {format_phone(phone)}")
