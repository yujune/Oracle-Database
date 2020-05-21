
import xlrd

css = []

workbook = xlrd.open_workbook('../Excel/Courses.xlsx')


for j in range(3):
    worksheet = workbook.sheet_by_index(j)
    for i in range(1, worksheet.nrows):
        cs = []
        cs.append(worksheet.cell_value(i,0))
        cs.append(worksheet.cell_value(i,1))
        cs.append(worksheet.cell_value(i,2))
        cs.append(worksheet.cell_value(i,3))
        cs.append(int(worksheet.cell_value(i,4)))
        cs.append(int(worksheet.cell_value(i,5)))
        cs.append(int(worksheet.cell_value(i,6)))
        css.append(cs)
    
    
with open('../Insert/in_04_Course.txt','w') as outFile:
    for cs in css:
        outFile.write("INSERT INTO Course VALUES ('{0}','{1}','{2}','{3}',{4},{5},{6});\n".format(
                        cs[0],
                        cs[1],
                        cs[2],
                        cs[3],
                        cs[4],
                        cs[5],
                        cs[6] ))
        
print(len(css))