import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service-account.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet
SHEET_ID = "1_VZDt17QjDlV7YrZhdXGrr7KrKMsOzBqM1T7xBnC2qo"
sheet = client.open_by_key(SHEET_ID).sheet1

# Function to Fetch Alumni Data
def get_alumni_data():
    return sheet.get_all_records()
