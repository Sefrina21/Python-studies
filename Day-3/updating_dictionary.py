employee = {
    "name": "Karthik",
    "age": 25,
    "department": "IT",
    "role": "Developer"
}

# Update history list
history = []

print("Before Update:")
print(employee)

# Save old values in history before updating
history.append(employee.copy())

# Updating employee details
employee["age"] = 26
employee["department"] = "AI & Data Science"
employee["role"] = "Senior Developer"
employee["location"] = "Chennai"

history.append(employee.copy())

print("\nAfter Update:")
print(employee)

print("\nUpdate History:")
for i, record in enumerate(history, start=1):
    print(f"\nVersion {i}:")
    print(record)
