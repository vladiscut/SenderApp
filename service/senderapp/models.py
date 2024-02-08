from django.utils import timezone
from django.db import models

class MailingList(models.Model):
    recipient = models.ManyToManyField('Recipient', blank=True)
    message = models.ManyToManyField('Message', blank=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_start = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_sending = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Recipient(models.Model):
    email = models.EmailField(unique=True)
    birth_date = models.DateField() 

    def __str__(self):
        return self.email
    
    def get_age(self):
        age = timezone.now().date() - self.birth_date
        return int(age.days / 365.25)


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

class SentMessage(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    mail_list = models.ForeignKey(MailingList, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.message.subject} - Recipient: {self.recipient.email}"