m1 = int(input(" Enter the marks of science: "))
m2 = int(input(" Enter the marks of maths: "))
m3 = int(input(" Enter the marks of english: "))
m4 = int(input(" Enter the marks of python: "))
m5 = int(input(" Enter the marks of geography: "))
avg = (m1 + m2 + m3 + m4 + m5) / 5
print ("average is: " , avg )

if avg >= 91 and avg <= 100:
    print("grade  A1") 
elif avg >= 81:
    print("grade A2")
elif avg >= 71:
    print("grade A3")
elif avg >= 61:
    print("grade B2")
elif avg >= 33:
    print("grade C")
else: 
    print("You have failed")








