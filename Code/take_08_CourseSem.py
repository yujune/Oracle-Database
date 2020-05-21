
import xlrd

courseSems = []

workbook = xlrd.open_workbook('../Excel/CourseSem.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    courseSem = []
    courseSem.append(int(worksheet.cell_value(i,0)))
    courseSem.append(worksheet.cell_value(i,1))
    courseSem.append(int(worksheet.cell_value(i,2)))
    courseSem.append(worksheet.cell_value(i,3))
    courseSem.append(worksheet.cell_value(i,4))
    courseSem.append(worksheet.cell_value(i,5))
    courseSems.append(courseSem)
 
    
with open('../Insert/in_08_CourseSem.txt','w') as outFile:
    for courseSem in courseSems:
        outFile.write("INSERT INTO CourseSem VALUES ({0},'{1}',{2},'{3}','{4}','{5}');\n".format(
                        courseSem[0],
                        courseSem[1],
                        courseSem[2],
                        courseSem[3],
                        courseSem[4],
                        courseSem[5] ))
        
print(len(courseSems))