
import xlrd

assesss = []

workbook = xlrd.open_workbook('../Excel/Assessment.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    assess = []
    assess.append(int(worksheet.cell_value(i,0)))
    assess.append(worksheet.cell_value(i,1))
    assess.append(worksheet.cell_value(i,2))
    assess.append(worksheet.cell_value(i,3))
    assess.append(int(worksheet.cell_value(i,4)))
    assess.append(int(worksheet.cell_value(i,5)))
    assess.append(worksheet.cell_value(i,6))
    assess.append(int(worksheet.cell_value(i,7)))
    assesss.append(assess)
    
    
with open('../Insert/in_11_Assessment.txt','w') as outFile:
    for assess in assesss:
        outFile.write("INSERT INTO Assessment VALUES ({0},'{1}','{2}','{3}',{4},{5},'{6}',{7});\n".format(
                        assess[0],
                        assess[1],
                        assess[2],
                        assess[3],
                        assess[4],
                        assess[5],
                        assess[6],
                        assess[7] ))
        
print(len(assesss))