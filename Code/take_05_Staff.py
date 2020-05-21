
import xlrd

staffs = []

workbook = xlrd.open_workbook('../Excel/Staff.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    staff = []
    staff.append(int(worksheet.cell_value(i,0)))
    staff.append(worksheet.cell_value(i,1))
    staff.append(worksheet.cell_value(i,2))
    staff.append(worksheet.cell_value(i,3))
    staff.append(worksheet.cell_value(i,4))
    staff.append(worksheet.cell_value(i,6))
    staff.append(worksheet.cell_value(i,7))
    staffs.append(staff)
    
with open('../Insert/in_05_Staff.txt','w') as outFile:
    for staff in staffs:
        outFile.write("INSERT INTO Staff VALUES ({0},'{1}','{2}','{3}','{4}','{5}','{6}');\n".format(
                        staff[0],
                        staff[1],
                        staff[2],
                        staff[3],
                        staff[4],
                        staff[5],
                        staff[6] ))
        
print(len(staffs))