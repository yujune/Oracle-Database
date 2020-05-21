
import xlrd

pcs = []

workbook = xlrd.open_workbook('../Excel/ProgrammeCourse.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    pc = []
    pc.append(worksheet.cell_value(i,0))
    pc.append(worksheet.cell_value(i,1))
    pc.append(worksheet.cell_value(i,2))
    pcs.append(pc)
    
    
with open('../Insert/in_07_ProgrammeCourse.txt','w') as outFile:
    for pc in pcs:
        outFile.write("INSERT INTO ProgrammeCourse VALUES ('{0}','{1}','{2}');\n".format(
                        pc[0],
                        pc[1],
                        pc[2] ))
        
print(len(pcs))