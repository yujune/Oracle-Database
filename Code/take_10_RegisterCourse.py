
import xlrd

regCourses = []

workbook = xlrd.open_workbook('../Excel/RegisterCourse.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    regCourse = []
    regCourse.append(int(worksheet.cell_value(i,0)))
    regCourse.append(worksheet.cell_value(i,1))
    regCourse.append(worksheet.cell_value(i,2))
    regCourse.append(worksheet.cell_value(i,3))
    regCourse.append(worksheet.cell_value(i,4))
    regCourse.append(int(worksheet.cell_value(i,5)))
    regCourse.append(int(worksheet.cell_value(i,6)))
    regCourses.append(regCourse)
 

with open('../Insert/in_10_RegisterCourse.txt','w') as outFile:
    for regCourse in regCourses:
        outFile.write("INSERT INTO RegisterCourse VALUES ({0},'{1}','{2}','{3}','{4}',{5},'{6}');\n".format(
                        regCourse[0],
                        regCourse[1],
                        regCourse[2],
                        regCourse[3],
                        regCourse[4],
                        regCourse[5],
                        regCourse[6] ))
        
print(len(regCourses))