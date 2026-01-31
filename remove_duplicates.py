"""
Remove Duplicate Records

Identifies and removes duplicate entries based on a unique key.
"""

people = [
    {"id": 1, "name": "John", "email": "john@email.com"},
    {"id": 2, "name": "Mary", "email": "mary@email.com"},
    {"id": 1, "name": "John", "email": "john@email.com"},
    {"id": 3, "name": "Bob", "email": "bob@email.com"},
    {"id": 2, "name": "Mary", "email": "mary@email.com"},
]

def remove_duplicates(records: list, key: str):
    """
    Remove duplicate dictionaries from a list
    using a specified unique key.
    """
    seen = set()
    unique_records = []

    for record in records:
        identifier = record.get(key)
        if identifier not in seen:
            seen.add(identifier)
            unique_records.append(record)

    return unique_records

print("REMOVING DUPLICATES")
print("-" * 20)

unique_people = remove_duplicates(people, "id")

print(f"Original records: {len(people)}")
print(f"Unique records:   {len(unique_people)}")
print("\nFinal dataset:")
for person in unique_people:
    print(f"ID {person['id']} - {person['name']}")
