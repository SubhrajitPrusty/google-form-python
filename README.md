# google-form-python

Simple instructions on how to read data from a google sheet

## Instructions

Get credentials : [https://gspread.readthedocs.io/en/latest/oauth2.html](https://gspread.readthedocs.io/en/latest/oauth2.html)

**You need both Drive API and Google Sheets API**

*Remember to share the sheet with the client_email in the credential file*
(e.g : "client_email": "api-name@project-name.iam.gserviceaccount.com",)

Install modules: `pip install -r requirements.txt`

Use the app demo: `python app.py`