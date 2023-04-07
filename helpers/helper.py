import smtplib
import json
import os
from datetime import datetime


def send_email(offer, provider, temp=0):
    """
    Send an email with the given offer and provider information.

    :param offer: (dict) Offer information to be sent in the email body.
    :param provider: (str) Provider name to be used as the email subject.
    :param temp: (int) Number of retries attempted if the first attempt fails.
    :return: (int) 1 if the email was sent successfully, 0 otherwise.
    """
    current_time = datetime.now().strftime("%H:%M:%S")
    secrets_file = secrets_checker()
    with open(secrets_file, "r") as f:
        secrets = json.load(f)
    try:
        recipient_email = secrets["reciepient"]["email"]
        sender_email = secrets["sender"]["email"]

        subject = provider
        body = json.dumps(offer)
        message = f"Subject: {subject}\n\n{body}"

        smtp_server = secrets["server"]["smptp_server"]
        smtp_port = secrets["server"]["port"]
        smtp_username = secrets["sender"]["email"]
        smtp_password = secrets["sender"]["password"]
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
        smtp_connection.starttls()
        smtp_connection.login(smtp_username, smtp_password)

        smtp_connection.sendmail(sender_email, recipient_email, message)
        smtp_connection.quit()

        print("[Email] sent ! ")
        return 1
    except Exception as e:
        if temp == 0:
            return send_email(
                offer["href"], f"[NEW OFFER] ({current_time}) ", temp=temp + 1
            )
        print(f"[Email] Body  {json.dumps(offer)}")
        print(f"[Email] not sent due to an error: {e}")
        return 0


def secrets_checker():
    """
    Check if secrets.json file exists. If not, create one with default values.
    Return the path to the secrets file.
    """
    secrets_path = os.path.join(os.getcwd(), "secrets.json")
    if os.path.exists(secrets_path):
        return secrets_path

    secrets = {
        "sender": {"email": "sender@example.com", "password": "senderpassword"},
        "recipient": {"email": "recipient@example.com"},
        "server": {"smtp_server": "smtp.example.com", "port": 587},
    }
    with open(secrets_path, "w") as secret_file:
        json.dump(secrets, secret_file, indent=4)

    raise Exception(
        f"A new secrets file has been created at {secrets_path}. You must set the credentials in the file."
    )
