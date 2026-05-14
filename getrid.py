studentData = {
    "id1" : {"name":"Nandinii" ,"class" : 8 , "subject" : "english"},
    "id2" : {"name" : "Alexia" ,"class" : 8 , "subject" : "maths" } ,
     "id3" : {"name":"Nandinii" ,"class" : 8 , "subject" : "english"}

    
}
result = {}
seen = []

for key,value in studentData.items():
    if value not in seen:
        seen.append(value)

        result[key] = value
    
print(result)
