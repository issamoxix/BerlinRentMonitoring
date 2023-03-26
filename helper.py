import smtplib
import json
import os

def send_email(offer, provider, temp=0):
    path =f"{os.path.join(os.getcwd(),'secrets.json')}"
    secrets = json.loads(open(path,"r").read())
    try:
        # Define the email sender and recipient
        recipient_email = secrets['reciepient']['email']
        sender_email = secrets['sender']['email']

        # Define the email message
        subject = f"{provider}"
        body = json.dumps(offer)
        message = f"Subject: {subject}\n\n{body}"
        # Connect to the SMTP server
        smtp_server = secrets['server']['smptp_server']
        smtp_port = 587
        smtp_username = secrets['sender']['email']
        smtp_password = secrets['sender']['password']
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        # Send the email
        smtp_connection.sendmail(sender_email, recipient_email, message)

        # Disconnect from the SMTP server
        smtp_connection.quit()
        print("Email sent ! ")
        return 1
    except Exception as e:
        if temp == 0:
            return send_email(offer["href"], provider, temp=temp + 1)
        print(f"Email not sent due to an error: {e}")
