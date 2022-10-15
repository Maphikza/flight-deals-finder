from twilio.rest import Client
import requests
import smtplib
import os


SHEET_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")
MY_EMAIL = os.environ.get("APP_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")
# SHEETY_AUTH = {
#     "Authorization": "Basic WmFtYmk6WmFtYmlycnJ0ODU3QEA"
# }
email_list = ["sips", "comm", "bell"]

class NotificationManager:

    def __init__(self):
        self.account_sid = os.environ.get("SID_KEY")
        self.auth_token = os.environ.get("AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
        self.message = None

    def send_notification(self, text):
        # response = requests.get(url=SHEET_API_ENDPOINT, headers=SHEETY_AUTH)
        # response.raise_for_status()
        # email_data = response.json()
        for email in email_list:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=APP_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=email,
                                    msg=f"Subject:Flight Deals\n\n{text}")

