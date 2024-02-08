from rest_framework import generics
from .models import MailingList, Recipient, Message, SentMessage
from .serializers import MailingListSerializer, RecipientSerializer, MessageSerializer, SentMessageSerializer

class MailingListListCreateAPIView(generics.ListCreateAPIView):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer

class MailingListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer

class RecipientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

class RecipientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer

class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class SentMessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = SentMessage.objects.all()
    serializer_class = SentMessageSerializer

class SentMessageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentMessage.objects.all()
    serializer_class = SentMessageSerializer
