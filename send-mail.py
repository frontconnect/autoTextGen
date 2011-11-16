#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys
import smtplib, email
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "your mail address"
SMTP_PASSWORD = "password"
SMTP_FROM = "name surname <your mail address>"
SMTP_CC = "name surname <cc mail address>"

def send_mail(recipient, subject, body_path, attachment_path):
    # Create a MIME-multipart message.
    msg = email.MIMEMultipart.MIMEMultipart()

    # Set the message body.
    body = email.MIMEText.MIMEText(open(body_path).read())

    # Read the attachment.
    attachment = email.MIMEBase.MIMEBase("text", "plain")
    attachment.set_payload(open(attachment_path).read())
    attachment.add_header("Content-Disposition", "attachment",
                          filename=os.path.basename(attachment_path))
    encoders.encode_base64(attachment)

    # Embed body and attachment into the message.
    msg.attach(body)
    msg.attach(attachment)

    # Set message headers.
    msg.add_header("From", SMTP_FROM)
    msg.add_header("Cc", SMTP_CC)
    msg.add_header("To", recipient)
    msg.add_header("Subject", subject)

    # Send the message.
    mailer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mailer.set_debuglevel(1)
    mailer.ehlo()
    mailer.starttls()
    mailer.ehlo()
    mailer.login(SMTP_USERNAME, SMTP_PASSWORD)
    mailer.sendmail(SMTP_FROM, [recipient, SMTP_CC], msg.as_string())
    mailer.close()

def parse_args():
    if len(sys.argv) != 5:
        print "Usage:", sys.argv[0], "<RECIPIENT> <SUBJECT> <BODY-FILE-PATH> <ATTACHMENT-FILE-PATH>"
        sys.exit(1)
    return (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

def main():
    (recipient, subject, body_path, attachment_path) = parse_args()
    send_mail(recipient, subject, body_path, attachment_path)

if __name__ == "__main__":
    main()
