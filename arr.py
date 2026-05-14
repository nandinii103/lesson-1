import array as arr
numbers = arr.array("i" , [1,3,5,3,5,7,9,3])
occur = numbers.count(3)
print(occur)
numbers.reverse()
print(numbers)