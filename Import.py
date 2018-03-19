import xlwt

#задаем кодировку будущей книги
book=xlwt.Workbook(encoding="utf-8")
#создание разделов
sheet1=book.add_sheet("Test_sheet")

#сохранение книги
book.save('Import.xlsx')
