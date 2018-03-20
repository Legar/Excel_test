# https://openpyxl.readthedocs.io/en/stable/

# Открыть книгу по имени файла
workbook = openpyxl.load_workbook('./Test.xlsx')

# Выбрать лист по имени
worksheet = workbook.get_sheet_by_name('Test')

# Ввод данных в ячейку
worksheet.cell('B1', 'test')
