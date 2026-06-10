patients = ["Harika", "Suba", "Harina"]

print("FOR LOOP OUTPUT")
for patient in patients:
    print("Patient:", patient)


doctors = ["Dr. Kumar", "Dr. Priya", "Dr. Ravi"]

print("ENUMERATE OUTPUT")
for index, doctor in enumerate(doctors, start=1):
    print(f"{index}. {doctor}")


count = 0
max_patients = 3

print("WHILE LOOP OUTPUT")
while count < max_patients:
    print(f"Checking Patient Record #{count + 1}")
    count += 1

print("All Patient Records Checked")
