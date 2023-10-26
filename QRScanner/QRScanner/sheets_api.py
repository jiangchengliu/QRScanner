import gspread
from oauth2client.service_account import ServiceAccountCredentials 
import pprint
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime

# Creates a new spreadshit with the name Title
def Sheet_Init(title):
    # Set up the credentials
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/rwhel/OneDrive/Desktop/Notes/College/.CLUBS/Upe/QRScanner/client_key.json', 
        scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Create a Google Sheets service
    service = build('sheets', 'v4', credentials=credentials)

    # Create a new Google Sheets document
    spreadsheet = service.spreadsheets().create(body={
        'properties': {
            'title': title
        }}).execute()

    # Extract the spreadsheet ID
    spreadsheet_id = spreadsheet['spreadsheetId']

    print(f"Created new Sheet with ID: {spreadsheet_id}")
    return spreadsheet_id

# Takes a spreadsheet ID and creates a new meeting date if the current date is not in the sheets
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

# Checks if a spreadsheet has a subsheet of the given name
def Sheet_Check(subsheet_name, spreadsheet_id):
    # Set up the credentials
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/rwhel/OneDrive/Desktop/Notes/College/.CLUBS/Upe/QRScanner/client_key.json', 
        scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Create a Google Sheets service
    service = build('sheets', 'v4', credentials=credentials)


    # Use the 'get' method to retrieve information about the spreadsheet
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

    # Search for the specified sheet in the list of sheets
    sheet_properties = next((sheet['properties'] for sheet in spreadsheet['sheets'] if sheet['properties']['title'] == subsheet_name), None)

    if sheet_properties:
        sheet_name = sheet_properties['title']
        print(f"The subsheet with title '{subsheet_name}' has the name: {sheet_name}")
        return True
    else:
        print(f"No subsheet found with title '{subsheet_name}'")
        return False

# Search the google sheets of the given sheet for a subsheet with the inputted title
def Sheet_Search(spreadsheet_id, subsheet_title):
    # Set up the credentials
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/rwhel/OneDrive/Desktop/Notes/College/.CLUBS/Upe/QRScanner/client_key.json', 
        scopes=['https://www.googleapis.com/auth/spreadsheets'])
    # Create a Google Sheets service
    service = build('sheets', 'v4', credentials=credentials)

    # Use the 'get' method to retrieve data from the specified subsheet
    response = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=subsheet_title).execute()
    values = response.get('values', [])
    print(values)
    print(not values)

    if not values:
        last_empty_column = 1
        last_empty_row = 1
    else:
        # Calculate the index of the last empty cell (cell with no data)
        last_empty_row = len(values)
        last_empty_column = len(values[-1])

    print(f"The index of the last empty cell in '{subsheet_title}' is (row: {last_empty_row}, column: {last_empty_column}).")
    return last_empty_row,last_empty_column

# When given a string input, takes the string and inputs into the next available slot
def Sheet_Add(input, spreadsheet_id):
    # Set up the credentials
    credentials = service_account.Credentials.from_service_account_file(
        'C:/Users/rwhel/OneDrive/Desktop/Notes/College/.CLUBS/Upe/QRScanner/client_key.json', 
        scopes=['https://www.googleapis.com/auth/spreadsheets'])

    # Create a Google Sheets service
    service = build('sheets', 'v4', credentials=credentials)
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

    #tracker
    tracker = 0

    #get the time to check the meeting 
    time = datetime.datetime.now()
    title = time.strftime("%Y-%m-%d")

    last_subsheet_index = len(spreadsheet['sheets']) - 1

    if Sheet_Check(title, spreadsheet_id):
        subsheet_index = last_subsheet_index = len(spreadsheet['sheets']) - 1
        insert_row, insert_column = Sheet_Search(spreadsheet_id,title)
        range_name = str(title+ '!'+ 'A' + str(insert_row+1))
    else:
        Sheet_Update(spreadsheet_id)    
        #find the sheet you want to edit
        subsheet_index = last_subsheet_index = len(spreadsheet['sheets']) - 1
        insert_row, insert_column = Sheet_Search(spreadsheet_id,title)
        range_name = str(title+'!'+ 'A' + str(insert_row+1))
    
    #Specify the Google Sheet ID and the range to update
    

    # Create a request to update the value
    value_input_option = 'RAW'  # Use 'RAW' for plain text
    value_range_body = {
    'values': [[input]]}

    request = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption=value_input_option,
        body=value_range_body)

    # Execute the request to update the value
    response = request.execute()

    print(f"Updated cell {range_name} with value: {input}")

Sheet_Add('rwhelan3@bu.edu','112CnwYraIIqFTKCZE8_3dq3LmIDNi9RsAcwJWE1TMAI')
Sheet_Add('ex@bu.edu','112CnwYraIIqFTKCZE8_3dq3LmIDNi9RsAcwJWE1TMAI')
Sheet_Add('example2', '112CnwYraIIqFTKCZE8_3dq3LmIDNi9RsAcwJWE1TMAI')
