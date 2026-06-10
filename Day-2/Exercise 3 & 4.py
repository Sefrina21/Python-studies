# EXERCISE 3

patients = []

patients.append("Harika")
patients.append("Suba")
patients.append("Harina")

print("Total Patients:", len(patients))

patients.pop(1)

print("Available Patients:", patients)


# EXERCISE 4

doctors = [
    {"department": "General", "name": "Dr. Kumar"},
    {"department": "Cardiology", "name": "Dr. Priya"},
    {"department": "General", "name": "Dr. Ravi"}
]

print("\nDoctors in General Department:")

for doctor in doctors:
    if doctor["department"] == "General":
        print(doctor["name"])
