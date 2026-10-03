students = {
    "bob": 85,
    "natasha": 93,
    "cindy": 78,
    "alyssa": 95,
    "aleksandra": 88
}

print("Student scores:")
for name, score in students.items():
    print(name, ":", score)


total = 0
for score in students.values():
    total += score
average = total / len(students)
print("Class average:", average)


highest_score = max(students.values())
lowest_score = min(students.values())

print("Highest score is:", highest_score)
print("Lowest score is:", lowest_score)


for name, score in students.items():
    if score == highest_score:
        print("The top student is", name)

for name, score in students.items():
    if score == lowest_score:
        print("The lowest student is", name)

search_name = input("Enter name of student: ").lower()

if search_name in students:
    print(search_name, "score is", students[search_name])
else:
    print("Student not found in system, try again")

