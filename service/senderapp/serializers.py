from rest_framework import serializers
from .models import MailingList, Recipient, Message, SentMessage

class MailingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailingList
        fields = ['name', 'created_at', 'is_active', 'is_sending', 'last_start']

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class SentMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentMessage
        fields = '__all__'
