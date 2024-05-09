from twilio.rest import Client
import sys
import os
sys.path.append(os.path.dirname("/Users/saravanakumar/PycharmProjects/pythonProject/Automation/utilities"))
from utilities import GlobalVariables

def readOTP(self):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    To_Number = ''
    messages = client.messages.list(to=To_Number)
    for message in messages:
        print(f"From: {message.from_},To: {message.to},Body: {message.body}")
        Messages = f"From: {message.from_},To: {message.to},Body: {message.body}"
        print(Messages[-6])
        GlobalVariables.OTP = Messages[-6]
        return GlobalVariables.OTP




