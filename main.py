import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def fetch_all_pages_from_site(api_key, cse_id, site):
    """Fetch all indexed pages from a specified site using Google Custom Search API."""
    url = "https://www.googleapis.com/customsearch/v1"
    results_list = []
    start_index = 1

    while True:
        params = {
            'key': api_key,
            'cx': cse_id,
            'q': f"site:{site}",
            'start': start_index
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching data: {response.json()}")
            break

        results = response.json()
        items = results.get('items', [])
        if not items:
            print("No more results found.")
            break
        results_list.extend([item['link'] for item in items])

        nextPage = results.get('queries', {}).get('nextPage', [])
        if nextPage:
            start_index = nextPage[0]['startIndex']
        else:
            break

    return results_list

def save_results_to_sheets(credentials_file, spreadsheet_name, worksheet_name, urls):
    """Save search results to Google Sheets."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    credentials = Credentials.from_service_account_file(credentials_file, scopes=scope)
    gc = gspread.authorize(credentials)

    try:
        spreadsheet = gc.open(spreadsheet_name)
    except gspread.exceptions.SpreadsheetNotFound:
        spreadsheet = gc.create(spreadsheet_name)
        spreadsheet.share('searchallurls@searchallurls.iam.gserviceaccount.com', perm_type='user', role='writer')
        print("Spreadsheet created and shared with your service account. Please refresh the Google Drive.")

    worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows=max(1, len(urls)) + 1, cols=1)
    worksheet.update('A1', [['URL']] + [[url] for url in urls])

    print(f"Results have been saved to the Google Sheet '{spreadsheet_name}' in the worksheet '{worksheet_name}'.")

def main(site, spreadsheet_name):
    """Main function to fetch URLs and save them to Google Sheets."""
    api_key = os.getenv("GOOGLE_API_KEY")
    cse_id = os.getenv("GOOGLE_CSE_ID")
    credentials_file = os.getenv("GOOGLE_CREDENTIALS_FILE")

    worksheet_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    urls = fetch_all_pages_from_site(api_key, cse_id, site)
    save_results_to_sheets(credentials_file, spreadsheet_name, worksheet_name, urls)
    return urls

if __name__ == "__main__":
    site = input("Enter the site URL: ")
    spreadsheet_name = input("Enter the name of the Google Sheet: ")
    urls = main(site, spreadsheet_name)
    print("Fetched URLs:")
    for url in urls:
        print(url)
