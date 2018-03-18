import openpyxl

#задаем кодировку будущей книги
book=openpyxl.Workbook(encoding="utf-8")
#создание разделов
sheet1=book.add_sheet("Test_sheet")

#сохранение книги
book.save('Import.xlsx')
