student_data = {
    "id1": {"name": "Alice", "class": "10A", "subject": "Math"},
    "id2": {"name": "Bob", "class": "10B", "subject": "Science"},
    "id3": {"name": "Alice", "class": "10A", "subject": "Math"},  # Duplicate record for Step 6
    "id4": {"name": "Charlie", "class": "10C", "subject": "History"}
}

print("Step 2: Original Records")
print(student_data)
print()

print("Access Values Safely")
print("id1:", student_data.get("id1", "Not Found"))
print("id5 (before adding):", student_data.get("id5", "Not Found"))
print()

print(" Add a New Student Record ")
student_data["id5"] = {"name": "Diana", "class": "10A", "subject": "English"}
print(student_data)
print()

print("Update an Existing Record ")
student_data["id2"]["subject"] = "Physics"
print("Updated id2:", student_data["id2"])
print()

print("Remove Duplicate Records")
cleaned_data = {}
seen_records = []

for student_id, details in student_data.items():
    record_tuple = (details["name"], details["class"], details["subject"])
    
    if record_tuple not in seen_records:
        seen_records.append(record_tuple)
        cleaned_data[student_id] = details

print("Cleaned Data:", cleaned_data)
print()

print("Remove One Record and Check Length ---")
removed_record = student_data.pop("id4")
print("Removed id4:", removed_record)
print("Remaining student records count:", len(student_data))
print()

print("Final Records ---")
for student_id, details in student_data.items():
    print(f"{student_id}: {details}")