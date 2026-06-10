employee = {
    "employee_name": "Rahul",
    "age": 28,
    "company": "Tech Solutions",
    "department": "Web Development",
    "employee_id": 102,
    "manager": "Mr. Kumar",
    "active": True
}

print(employee)
print(employee["employee_name"])
print(employee["manager"])
print(employee["employee_id"])
print(employee.get("salary", "Not Available"))
