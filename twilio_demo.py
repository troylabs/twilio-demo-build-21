# This script is a demo for how to use Twilio
# This uses Python but many other languages are available

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from dotenv import load_dotenv
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
# load_dotenv() loads in the environment variables, which should be in your .env file
# NEVER push your .env file, that should stay on your local computer only
load_dotenv()

# Twilio account information is imported from environment and stored here in variables.
# It is not hardcoded into the code
# This is a security practice to protect confidential information
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# initializing the Twilio client
client = Client(account_sid, auth_token)


def send_text_message(sending_number, receiving_number, message):
    # This function creates and send the message through Twilio
    message = client.messages.create(
        body=message,
        from_=sending_number,
        to=receiving_number
    )

    # This line just prints the id of the successful message
    print(message.sid)


if __name__ == '__main__':
    # this is the number associated with your twilio account for sending messages
    sender_number = "+1xxxxxxxxxxx"

    # this number is who will receive the message (usually one of your users)
    recipient_number = "+1xxxxxxxxxxx"
    message_body = "This is a filler message!"

    # here we are calling the function to send a message and passing in the relevant information
    send_text_message(sender_number, recipient_number, message_body)
