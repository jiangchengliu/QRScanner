import gspread
from oauth2client.service_account import ServiceAccountCredentials 
import pprint
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

#Fetch the sheet
sheet = client.open('Tester').sheet1
python_sheet = sheet.get_all_records()
pp = pprint.PrettyPrinter()
pp.pprint(python_sheet)

#Insert Row
input = "what do you want to put in the sheets?"
row = [input]
index = 1
sheet.insert_row(row,index)

def Sheet_Init():
    # Set up the credentials
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/rwhel/OneDrive/Desktop/Notes/College/.CLUBS/Upe/QRScanner/client_key.json', 
        scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Create a Google Sheets service
    service = build('sheets', 'v4', credentials=credentials)

    # Create a new Google Sheets document
    spreadsheet = service.spreadsheets().create(body={
        'properties': {
            'title': 'UPE_attendance_sheet'
        }}).execute()

    # Extract the spreadsheet ID
    spreadsheet_id = spreadsheet['spreadsheetId']

    print(f"Created new Sheet with ID: {spreadsheet_id}")
    return spreadsheet_id

def Sheet_Update(spreadsheet_id):
    time = datetime.datetime.now()
    title = time.strftime("%Y-%m-%d")

     # Set up the credentials
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/rwhel/OneDrive/Desktop/Notes/College/.CLUBS/Upe/QRScanner/client_key.json', 
        scopes=['https://www.googleapis.com/auth/spreadsheets'])


    # Create a Google Sheets service
    service = build('sheets', 'v4', credentials=credentials)

    # Create a request to add a new subsheet
    add_sheet_request = {
        "requests": [
            {
                "addSheet": {
                    "properties": {
                        "title": title
                    }
                }
            }
        ]
    }

    # Execute the request to add the new subsheet
    response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=add_sheet_request).execute()

    # Extract the ID of the newly created subsheet
    new_sheet_id = response['replies'][0]['addSheet']['properties']['sheetId']

    print(f"Created a new subsheet with ID: {new_sheet_id}")

Sheet_Update('112CnwYraIIqFTKCZE8_3dq3LmIDNi9RsAcwJWE1TMAI')