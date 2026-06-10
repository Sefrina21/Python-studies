# Exercise 1:
name = "Winzy"
area = "Puduppalaiyam"
problem = "Garbage on the road"
print(f"Report: {problem} at {area} by {name}")

#Exercise 2:
def check_photo(photo_uploaded):
    if photo_uploaded:
        print("Photo attached ✓")
    else:
        print("No photo - please upload one")

check_photo(True)
check_photo(False)
