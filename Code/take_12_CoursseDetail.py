
import xlrd

cDetails = []

workbook = xlrd.open_workbook('../Excel/CourseDetail.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    cDetail = []
    cDetail.append(int(worksheet.cell_value(i,0)))
    cDetail.append(int(worksheet.cell_value(i,1)))
    cDetail.append(worksheet.cell_value(i,2))
    cDetail.append(worksheet.cell_value(i,3))
    cDetail.append(int(worksheet.cell_value(i,4)))
    cDetails.append(cDetail)
    
    
with open('../Insert/in_12_CourseDetail.txt','w') as outFile:
    for cDetail in cDetails:
        outFile.write("INSERT INTO CourseDetail VALUES ({0},{1},'{2}','{3}',{4});\n".format(
                        cDetail[0],
                        cDetail[1],
                        cDetail[2],
                        cDetail[3],
                        cDetail[4] ))
        
print(len(cDetails))