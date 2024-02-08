import time
from .models import MailingList
# from huey import SqliteHuey

# huey = SqliteHuey(filename='huey.db')


#функция заглушка, имимтация отправки письма
# @huey.task()
def send_mail():
    time.sleep(3)
    print('huey')
    

# @huey.task()
def send_emails_to_recipients(mailing_list):
    print(mailing_list)
    recipients = mailing_list.recipient.all()
    messages = mailing_list.message.all()
    
    for message in messages:
        subject = message.subject
        body = message.body 
        for recipient in recipients:
            print(recipient)
            to_email = recipient.email
            send_mail()

    # mailing_list.is_sending = False
    # mailing_list.save()

