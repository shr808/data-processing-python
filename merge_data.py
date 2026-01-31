"""
Merge Data from Multiple Sources

Combines records from two systems using a shared identifier.
"""

system_a = [
    {"id": 101, "name": "Alice", "role": "Manager"},
    {"id": 102, "name": "Bob", "role": "Developer"},
    {"id": 103, "name": "Charlie", "role": "Analyst"},
]

system_b = [
    {"id": 102, "name": "Robert", "department": "IT"},
    {"id": 104, "name": "Diana", "department": "HR"},
    {"id": 105, "name": "Eve", "department": "Finance"},
]

def merge_data(source_a: list, source_b: list, key: str = "id") -> list:
    """
    Merge two lists of dictionaries using a shared key.
    Later sources override earlier values.
    """
    merged = {}

    for record in source_a + source_b:
        record_id = record.get(key)
        merged.setdefault(record_id, {}).update(record)

    return list(merged.values())

print("MERGING DATA FROM MULTIPLE SYSTEMS")
print("-" * 35)

merged_data = merge_data(system_a, system_b)

for record in merged_data:
    print(record)
