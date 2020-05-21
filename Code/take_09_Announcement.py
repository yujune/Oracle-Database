
import xlrd

announs = []

workbook = xlrd.open_workbook('../Excel/Announcement.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    announ = []
    announ.append(int(worksheet.cell_value(i,0)))
    announ.append(worksheet.cell_value(i,1))
    announ.append(worksheet.cell_value(i,2))
    announ.append(worksheet.cell_value(i,3))
    announ.append(worksheet.cell_value(i,4))
    announ.append(int(worksheet.cell_value(i,5)))
    announs.append(announ)
 
    
with open('../Insert/in_09_Announcement.txt','w') as outFile:
    for announ in announs:
        outFile.write("INSERT INTO Announcement VALUES ({0},'{1}','{2}','{3}','{4}',{5});\n".format(
                        announ[0],
                        announ[1],
                        announ[2],
                        announ[3],
                        announ[4],
                        announ[5] ))
        
print(len(announs))