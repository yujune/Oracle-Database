
import xlrd

assesss = []

workbook = xlrd.open_workbook('../Excel/LearnerAssessment.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    assess = []
    assess.append(int(worksheet.cell_value(i,0)))
    assess.append(int(worksheet.cell_value(i,1)))
    assess.append(float(worksheet.cell_value(i,2)))
    assess.append(worksheet.cell_value(i,3))
    assess.append(worksheet.cell_value(i,4))
    assesss.append(assess)
    
    
with open('../Insert/in_16_LearnerAssessment.txt','w') as outFile:
    for assess in assesss:
        outFile.write("INSERT INTO LearnerAssessment VALUES ({0},'{1}',{2:.1f},'{3}','{4}');\n".format(
                        assess[0],
                        assess[1],
                        assess[2],
                        assess[3],
                        assess[4] ))
        
print(len(assesss))