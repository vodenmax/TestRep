import csv
students=[]
with open("D:\docs\Student-627\Downloads\students.csv", encoding="utf8") as file:
    reader = csv.DictReader(file, delimiter = ',')
    for student in reader:
      students.append({'id': student['id'], 'name': student['name'], 'titleProject_id': student['titleProject_id'], 'class': student['class'], 'score': student['score']})
print(students)