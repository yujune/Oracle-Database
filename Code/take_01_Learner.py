
import xlrd

learners = []

workbook = xlrd.open_workbook('../Excel/Learner.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    learner = []
    learner.append(int(worksheet.cell_value(i,0)))
    learner.append(worksheet.cell_value(i,1))
    learner.append(worksheet.cell_value(i,2))
    learner.append(worksheet.cell_value(i,3))
    learner.append(worksheet.cell_value(i,4))
    learner.append(worksheet.cell_value(i,5))
    learner.append(worksheet.cell_value(i,6))
    learner.append(worksheet.cell_value(i,7))
    learner.append(worksheet.cell_value(i,8))
    learners.append(learner)


with open('../Insert/in_01_Learner.txt','w') as outFile:
    for learner in learners:
        outFile.write("INSERT INTO Learner VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}');\n".format(
                        learner[0],
                        learner[1],
                        learner[2],
                        learner[3],
                        learner[4],
                        learner[5],
                        learner[6],
                        learner[7],
                        learner[8] ))
        
print(len(learners))