num1 = [2,3,1]
num2 = ["b","a","c"]
num3 = list(zip(num1 ,num2))
print(num3)
num4 = list(zip(num1,num2[0 :: -1]))
print(num4)
num5 = dict(zip(num1 ,num2))
print(num5)