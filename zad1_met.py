import csv
with open("D:\docs\Student-627\Downloads\students.csv", encoding="utf8") as file:
    reader = csv.reader(file,delimiter=',',quotechar='"')
    students=list(reader)[1:]
    print(students)
    for id,name,title,clas,score in students:
        if "Хадаров" in name:
            print(f'Ты получил: {score}')
    count_class={}
    sum_class={}
    for id,name,title,clas,score in students:
        count_class[clas]= count_class.get(clas,0)+1
        sum_class[clas] = count_class.get(clas,0) + int(score if score != 'None' else 0)
    for id,name,title,clas,score in students:
        if score=='None':
            score=round(sum_class[clas]/count_class[clas],3)
with open('students_new','w',newline='',encoding='utf8')as f:
    w=csv.writer(f)
    w.writerow(['id','Name','titleProject_id','class','score'])
    w.writerows(students)