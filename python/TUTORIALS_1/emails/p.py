import smtplib
import ssl

def send_email(sender_email, receiver_email, password, subject, body):
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL
    sender_email = sender_email
    receiver_email = receiver_email
    password = password

    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print("Email sent successfully!")

# Usage example:
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
password = "your_app_password"  # Use application-specific password
subject = "Test Email"
body = "Hello, this is a test email!"

send_email(sender_email, receiver_email, password, subject, body)
