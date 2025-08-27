import smtplib
from email.message import EmailMessage

import authenticator

# This scripts sends an email with the key to the user for authentication purposes.


app_password = "" # App password for the email account

def send_email(to_email, sender, subject, body, attachment_path=None):
    # Create the email message
    msg = EmailMessage() # Create a new EmailMessage object
    msg['From'] = sender # Set the sender's email address
    msg['To'] = to_email # Set the recipient's email address
    msg['Subject'] = subject # Set the email subject
    msg.set_content(body) # Set the email body

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email_server:
        email_server.login(sender, app_password)
        email_server.send_message(msg) # Send the email message
        print("Email sent successfully.")


key = "" # The key should be generated and stored securely for each user
sender_email = "" # Sender's email address
recipient_email = "" # Recipient's email address
subject = "Here is your authentication key" # Email subject
body = f"Thank you for using our service, here is you authentication key: {authenticator.generate_totp(key)}" # Email body

send_email(recipient_email, sender_email, subject, body)

response = input("Enter the key you received via email: ")

if response == authenticator.generate_totp(key):
    print("Authentication successful!")
else:
    print("Authentication failed. Invalid key.")