
import xlrd

topics = []

workbook = xlrd.open_workbook('../Excel/Topic.xlsx')
worksheet = workbook.sheet_by_index(0)

for i in range(1, worksheet.nrows):
    topic = []
    topic.append(int(worksheet.cell_value(i,0)))
    topic.append(int(worksheet.cell_value(i,1)))
    topic.append(int(worksheet.cell_value(i,2)))
    topic.append(worksheet.cell_value(i,3))
    topic.append(worksheet.cell_value(i,4))
    topic.append(worksheet.cell_value(i,5))
    topics.append(topic)
    
    
with open('../Insert/in_15_Topic.txt','w') as outFile:
    for topic in topics:
        outFile.write("INSERT INTO Topic VALUES ({0},{1},{2},'{3}','{4}','{5}');\n".format(
                        topic[0],
                        topic[1],
                        topic[2],
                        topic[3],
                        topic[4],
                        topic[5] ))
        
print(len(topics))