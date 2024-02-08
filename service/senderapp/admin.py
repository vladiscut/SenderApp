from django.contrib import admin
from senderapp.models import *
from celery.result import AsyncResult
from .tasks import send_emails_to_recipients
# Register your models here.

def send_emails(modeladmin, request, queryset):
    for mailing_list in queryset:
        send_emails_to_recipients.delay(mailing_list.id)
        # print(result_send_task.id)

send_emails.short_description = "Send Emails"  # Описание действия в админ-панели

# Функция для отмены задачи
def cancel_send_emails(modeladmin, request, queryset):
    for mailing_list in queryset:
        # Получаем объект задачи по ее ID
        async_result = AsyncResult(mailing_list.task_id)
        # Отменяем задачу
        async_result.revoke()  # Отмена задачи
        mailing_list.is_sending = False
        mailing_list.save()

cancel_send_emails.short_description = "Cancel send Emails"  # Описание действия в админ-панели


class MailingListAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'is_active', 'is_sending', 'last_start']
    readonly_fields = ['is_sending', 'last_start']
    filter_horizontal = ('recipient', 'message')
    actions = [send_emails, cancel_send_emails]  # Добавляем действие к админ-модели

admin.site.register(MailingList, MailingListAdmin)
admin.site.register(Recipient)
admin.site.register(Message)
admin.site.register(SentMessage)