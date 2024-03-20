import csv
students=[]
with open("D:\docs\Student-627\Downloads\students.csv", encoding="utf8") as file:
    reader = csv.DictReader(file, delimiter = ',')
    for student in reader:
      students.append({'id': student['id'], 'name': student['name'], 'titleProject_id': student['titleProject_id'], 'class': student['class'], 'score': student['score']})
for student in students:
    if 'Хадаров' in student['name']:
        score = student['score']
        title = student['titleProject_id']
        print(f'Ты получил:{score}, за проект - {title}')
summ=0
k=0
for student in students:
    if student['score']!='None':
        summ+=int(student['score'])
        k+=1
summ=round(summ/k,3)
for student in students:
    if student['score']=='None':
        student['score']=summ


