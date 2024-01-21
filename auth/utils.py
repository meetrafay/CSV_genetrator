
from django.core.mail import EmailMessage
import os
from authentication import settings
from django.core.mail import send_mail


def send_welcome_email(recipient_email):
    subject = 'Your CSV Data'
    message = 'Attached is your CSV data.'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [recipient_email]

    # Attach the CSV file
    csv_file_path = os.path.join(settings.BASE_DIR, 'auth', './temp/SampleCSVFile_11kb.csv')
    
    # Create EmailMessage instance
    email_message = EmailMessage(subject, message, from_email, recipient_list)
    email_message.attach_file(csv_file_path)
    # Send the email
    email_message.send()


