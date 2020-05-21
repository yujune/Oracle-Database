
import xlrd

lps = []

workbook = xlrd.open_workbook('../Excel/LearnerProgramme.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    lp = []
    lp.append(int(worksheet.cell_value(i,0)))
    lp.append(worksheet.cell_value(i,1))
    lp.append(worksheet.cell_value(i,2))
    lp.append(int(worksheet.cell_value(i,3)))
    lps.append(lp)
    
    
with open('../Insert/in_06_LearnerProgramme.txt','w') as outFile:
    for lp in lps:
        outFile.write("INSERT INTO LearnerProgramme VALUES ('{0}','{1}','{2}',{3});\n".format(
                        lp[0],
                        lp[1],
                        lp[2],
                        lp[3] ))
        
print(len(lps))