employees = [
    {"id": 201, "name": "Karthik", "department": "IT", "role": "Developer"},
    {"id": 202, "name": "Priya", "department": "HR", "role": "Recruiter"},
    {"id": 203, "name": "Vikram", "department": "Finance", "role": "Analyst"}
]

# Display employee list
for e in employees:
    print(f"[{e['id']}] {e['name']} - {e['department']} ({e['role']})")


# Function to register new employee
def register_employee(name, age, department, role):
    return {
        "name": name,
        "age": age,
        "department": department,
        "role": role
    }

# Adding a new employee
employee = register_employee("Meera", 28, "IT", "Tester")

print(employee)
