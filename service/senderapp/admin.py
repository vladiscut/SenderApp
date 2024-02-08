from django.contrib import admin
from senderapp.models import *
from .tasks import send_emails_to_recipients
# Register your models here.

def send_emails(modeladmin, request, queryset):
    for mailing_list in queryset:
        # print(queryset)
        # Здесь вы можете вызвать ваш метод для отправки электронных писем
        # Например, send_emails_to_recipients(mailing_list.recipient.all(), mailing_list.message)
        mailing_list.is_sending = True
        mailing_list.save()
        send_emails_to_recipients(mailing_list)

send_emails.short_description = "Send Emails"  # Описание действия в админ-панели
   

class MailingListAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'is_active', 'is_sending', 'last_start']
    readonly_fields = ['is_sending', 'last_start']
    filter_horizontal = ('recipient', 'message')
    actions = [send_emails]  # Добавляем действие к админ-модели

admin.site.register(MailingList, MailingListAdmin)
admin.site.register(Recipient)
admin.site.register(Message)
admin.site.register(SentMessage)