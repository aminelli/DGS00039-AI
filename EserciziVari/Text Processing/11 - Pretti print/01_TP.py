import pprint

student_dict = {'Name': 'Tusar', 'Class': 'XII', 
     'Address': {'FLAT ':1308, 'BLOCK ':'A', 'LANE ':2, 'CITY ': 'HYD'}}

print (student_dict)
print ("\n")
print ("***With Pretty Print***")
print ("-----------------------")
pprint.pprint(student_dict,width=-1)
