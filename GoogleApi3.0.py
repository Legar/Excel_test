# Указанный метод работае только для устаревшего API 3.0 https://github.com/burnash/gspread

import gspread

# Авторизация
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('PyTableTest-44aed3e5ab67.json', scope)

gc = gspread.authorize(credentials)

# Открываем книгу по ссылке
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1B1oVSjtLNZXvoHSVCpAqNkmkVUFUDr1NDUI-hmD_zFA/edit?ts=5aafc6b6#gid=0')

# Добавляем и именуем лист
name_workcheet = input('введите имя книги: ')
worksheet = sh.add_worksheet(title=name_workcheet, rows="8", cols="10")

# Копируем данные из одной книги в другую
worksheet1 = sh.worksheet("https://docs.google.com/spreadsheets/d/1e2a7lGrhojc1mO_MbMRy7fcmG1eMKjF_yaQbh989UCg/edit?ts=5aafe461#gid=0")

# По циклу копируем значение значение первой строки

val1 = worksheet1.acell('B1').value

worksheet = sh.worksheet(name_workcheet)
worksheet.update_cell('B1', val1)

# открыть документ по ключу
# sht1 = gc.open_by_key('0BmgG6nO_6dprdS1MN3d3MkdPa142WFRrdnRRUWl1UFE')

# работать с документом по ссылке
# wks = gc.open_by_url(("").sheet1

# выборка по наименованию
# worksheet = sheet1.worksheet("19.03.2018")

# удаление книги
# sh.del_worksheet(worksheet)

# создание книги
# worksheet = sheet1.add_worksheet(title="A worksheet", rows="100", cols="20")

# Создание эл.таблицы
# sh = worksheet.create('A new spreadsheet')

# Шара созданной книги
# sh.share('Logeru@gmail.com', perm_type='user', role='writer')
