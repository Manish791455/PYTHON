graphic_students = ['manish', 'mohmmad', 'sandeep', 'prasanth', 'darpan']
web_students = []
for student in graphic_students:
    #if student name is sandeep leave him
    if student == 'sandeep':
        continue
    else:     
        web_students.append(student)
print('the list of web developer students is :', web_students)            
