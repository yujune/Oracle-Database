
import xlrd

lAnnouns = []

workbook = xlrd.open_workbook('../Excel/LearnerAnnouncement.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    lAnnoun = []
    lAnnoun.append(int(worksheet.cell_value(i,0)))
    lAnnoun.append(int(worksheet.cell_value(i,1)))
    lAnnoun.append(int(worksheet.cell_value(i,2)))
    lAnnouns.append(lAnnoun)
    
    
with open('../Insert/in_14_LearnerAnnouncement.txt','w') as outFile:
    for lAnnoun in lAnnouns:
        outFile.write("INSERT INTO LearnerAnnouncement VALUES ({0},'{1}',{2});\n".format(
                        lAnnoun[0],
                        lAnnoun[1],
                        lAnnoun[2] ))
        
print(len(lAnnouns))