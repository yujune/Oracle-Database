
import xlrd

sems = []

workbook = xlrd.open_workbook('../Excel/Semester.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    sem = []
    sem.append(int(worksheet.cell_value(i,0)))
    sem.append(worksheet.cell_value(i,1))
    sem.append(worksheet.cell_value(i,2))
    sem.append(worksheet.cell_value(i,3))
    sem.append(worksheet.cell_value(i,4))
    sems.append(sem)
    

with open('../Insert/in_03_Semester.txt','w') as outFile:
    for sem in sems:
        outFile.write("INSERT INTO Semester VALUES ({0},'{1}','{2}','{3}','{4}');\n".format(
                        sem[0],
                        sem[1],
                        sem[2],
                        sem[3],
                        sem[4] ))
        
print(len(sems))