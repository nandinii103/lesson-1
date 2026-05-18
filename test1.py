student =  {
    "Bob": 29,
    "Alex": 35,
    "nice": 67,
    "Nancy":89,
    "June": 93
}

for name,score in student.items():
    print(name, ":" , score)

total = 0 
for score in student.values():
    total = total + score
average = total / len(student)
print(average)

    