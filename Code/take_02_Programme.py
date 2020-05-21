
import xlrd

progs = []

workbook = xlrd.open_workbook('../Excel/Programme.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    prog = []
    prog.append(worksheet.cell_value(i,0))
    prog.append(worksheet.cell_value(i,1))
    prog.append(worksheet.cell_value(i,2))
    prog.append(int(worksheet.cell_value(i,3)))
    progs.append(prog)


with open('../Insert/in_02_Programme.txt','w') as outFile:
    for prog in progs:
        outFile.write("INSERT INTO Programme VALUES ('{0}','{1}','{2}',{3});\n".format(
                        prog[0],
                        prog[1],
                        prog[2],
                        prog[3] ))
        
print(len(progs))