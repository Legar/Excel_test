import xlrd

workbook = xlrd.open_workbook('./Export.xls')
#Читаем данные с первого листа
worksheet = workbook.sheet_by_index(0)
#Читаем данные по имени листа
#worksheet = workbook.sheet_by_name('Name')
#печатаем данные из ячейки
print('row 3 and colomn 2 is : {0}'.format(worksheet.cell(3,2).value))
