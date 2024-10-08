from celery import shared_task
import smtplib
import os
from email.message import EmailMessage

#PHONE_NUMBER & CARRIER should come from database

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
CARRIER = os.getenv("CARRIER")

HOST = "smtp.gmail.com"
PORT_NUMBER = 587

SMS_CARRIERS = {
    "AT&T": "@txt.att.net",
    "Sprint": "@messaging.sprintpcs.com",
    "T-Mobile": "@tmomail.net",
    "Verizon": "@vtext.com",
    "Metro PCS": "@mymetropcs.com",
}

@shared_task
def send_email(new_vehicles):
    msg_sms = create_message(new_vehicles, PHONE_NUMBER, CARRIER)
    msg_email = create_message(new_vehicles, EMAIL_ADDRESS, None)
    with smtplib.SMTP(HOST, PORT_NUMBER) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        smtp.send_message(msg_sms)
        smtp.send_message(msg_email)
        smtp.close()

@shared_task
def create_message(new_vehicles, recipient, carrier) -> EmailMessage:

    msg = EmailMessage()
    msg["To"] = (
        EMAIL_ADDRESS if carrier is None else f"{recipient}{SMS_CARRIERS[CARRIER]}"
    )
    msg["From"] = EMAIL_ADDRESS
    msg["Subject"] = "New Postings!"
    msg.set_content(format_content(new_vehicles))

    return msg

@shared_task
def format_content(new_vehicles):
    msg_content = ""
    for key in new_vehicles:
        msg_content += f"\nLocation: {key}\n\n"
        for car in new_vehicles[key]:
            msg_content += f'Vehicle: {car["Car"]}\nVIN: {car["VIN"]}\nRow Number: {car["Row"]}\nLink to Posting: {car["Link"]}\n\n'

    return msg_content