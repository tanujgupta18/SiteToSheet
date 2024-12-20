# **SiteToSheet**

**SiteToSheet** is a Python script that fetches all indexed URLs from a specified website using the Google Custom Search API and saves the results to a Google Sheets document. The script is built as a Flask web application and securely stores sensitive information, like API keys and credentials, using environment variables.

## **Features**

- Fetches all indexed URLs from a specified website using the Google Custom Search API.
- Saves the fetched URLs to a Google Sheets document.
- Secure handling of sensitive credentials via environment variables and Render secrets.
- A simple Flask web interface to run the script.

## **Prerequisites**

Before running the application, you need to set up the following:

1. **Google Custom Search API Key**: Obtain a valid API key from the [Google Cloud Console](https://console.cloud.google.com/).
2. **Google Custom Search Engine (CSE) ID**: Create a custom search engine at [Google CSE](https://cse.google.com/cse/) and get your CSE ID.
3. **Google Service Account Credentials**: Create a service account in your Google Cloud project and generate a JSON credentials file for accessing Google Sheets.

## **Setup**

### 1. Clone the Repository

```bash
git clone https://github.com/tanujgupta18/SiteToSheet.git
cd SiteToSheet
```

### 2. Install Dependencies

The script requires the following Python libraries:

- `Flask`: A lightweight WSGI web application framework for Python.
- `requests`: To make HTTP requests to the Google Custom Search API.
- `gspread`: To interact with Google Sheets.
- `google-auth`: For Google authentication.
- `python-dotenv`: To load environment variables from a `.env` file.

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

To securely store sensitive data (API keys, CSE ID, and credentials), create a `.env` file in the root of the project and add the following variables:

```env
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id
GOOGLE_CREDENTIALS_JSON="your_google_service_account_json_as_a_string"
```

Make sure to replace `your_google_api_key`, `your_custom_search_engine_id`, and `your_google_service_account_json_as_a_string` with your actual values. You can paste the contents of your service account JSON file into the `GOOGLE_CREDENTIALS_JSON` variable as a string.

### 4. Create and Share a Google Sheet

Ensure that you have a Google Sheet where the results will be saved. If the sheet doesn't exist, the script will create a new one and share it with your service account email. You will need to share the Google Sheets document with the service account email provided in your service account JSON credentials file.

## **Usage**

### 1. Run the Flask Application Locally

To run the Flask app locally, simply execute the following command:

```bash
python app.py
```

Once the application is running, open your browser and navigate to `http://127.0.0.1:5000`. You will be prompted to:

- **Site URL**: Enter the website from which to fetch indexed pages (e.g., `example.com`).
- **Google Sheet Name**: Enter the name of the Google Sheet where the URLs will be saved.

### 2. Run the Script via Flask Interface

The Flask web interface will allow you to input the site URL and Google Sheet name through a form. The script will fetch the indexed URLs and save them to the specified Google Sheet.

### 3. Output

The script will create a new worksheet in the specified Google Sheet. The worksheet name will be the current timestamp (e.g., `2024-12-20_14-30-00`), and it will contain the list of indexed URLs.
