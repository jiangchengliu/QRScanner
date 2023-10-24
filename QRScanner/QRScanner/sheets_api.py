import gspread
from oauth2client.service_account import ServiceAccountCredentials 
import pprint
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime




# Set up the credentials
credentials = service_account.Credentials.from_service_account_file(
    'C:\Users\rwhel\OneDrive\Desktop\Notes\College\.CLUBS\Upe\QRScanner\client_key.json', 
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)

# Create a Google Sheets service
service = build('sheets', 'v4', credentials=credentials)

# Create a new Google Sheets document
spreadsheet = service.spreadsheets().create(body={
    'properties': {
        'title': 'UPE_attendance_sheet'
    }
}).execute()

# Extract the spreadsheet ID
spreadsheet_id = spreadsheet['spreadsheetId']

print(f"Created new Dub Sheet with ID: {spreadsheet_id}")

title = datetime.datetime.now()

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

