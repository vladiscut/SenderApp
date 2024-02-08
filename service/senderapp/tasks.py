import time
from .models import MailingList
from celery import shared_task


@shared_task()
def send_emails_to_recipients(mailing_list_id):
    # print(mailing_list)
    mailing_list = MailingList.objects.get(id=mailing_list_id)
    print(mailing_list)
    recipients = mailing_list.recipient.all()
    messages = mailing_list.message.all()
    
    if recipients and messages:
        mailing_list.is_sending = True
        mailing_list.save()

        for message in messages:
            subject = message.subject
            body = message.body 
            i=0
            for recipient in recipients:
                # print(recipient)
                print(i)
                i+=1
                to_email = recipient.email
                send_mail(subject, body, to_email)

        mailing_list.is_sending = False
        mailing_list.save()

#функция заглушка, имимтация отправки письма
def send_mail(subject, body, to_email):
    time.sleep(3)
    