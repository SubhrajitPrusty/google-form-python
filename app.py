import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


# get credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# create a gspread client with the credentials
gc = gspread.authorize(credentials)

# get all workbooks
workbooks = gc.openall()

print(workbooks)


# open the first sheet of the first workbook
sheet = workbooks[0].get_worksheet(0)

print(sheet)


# get all values in the sheet as list of lists (like a csv file)
data = sheet.get_all_values()

print(data)