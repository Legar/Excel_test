import httplib2
import apiclient.discovery
import gspread
import oauth2client.service_account

#Создание сервис обьектов для работы с гугл таблицами
CREDENTIALS_FILE = "PyTableTest-44aed3e5ab67.json"  # имя файла с закрытым ключом

credentials = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

#Create Google Table

spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Тянка тест1', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
}).execute()

#Share for email
driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
shareRes = driveService.permissions().create(
    fileId = spreadsheet['spreadsheetId'],
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'Logeru@gmail.com'},
    fields = 'id'
).execute()