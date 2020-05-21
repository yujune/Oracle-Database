
import xlrd

assignStaffs = []

workbook = xlrd.open_workbook('../Excel/AssignStaff.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    assignStaff = []
    assignStaff.append(int(worksheet.cell_value(i,0)))
    assignStaff.append(int(worksheet.cell_value(i,1)))
    assignStaff.append(worksheet.cell_value(i,2))
    assignStaffs.append(assignStaff)
    

with open('../Insert/in_13_AssignStaff.txt','w') as outFile:
    for assignStaff in assignStaffs:
        outFile.write("INSERT INTO AssignStaff VALUES ({0},{1},'{2}');\n".format(
                        assignStaff[0],
                        assignStaff[1],
                        assignStaff[2] ))
        
print(len(assignStaffs))