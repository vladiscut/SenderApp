from django.urls import path
from . import views

urlpatterns = [
    path('mailing-list/', views.MailingListListCreateAPIView.as_view(), name='mailing-list'),
    path('mailing-list/<int:pk>/', views.MailingListRetrieveUpdateDestroyAPIView.as_view(), name='mailing-list-detail'),
    path('recipient/', views.RecipientListCreateAPIView.as_view(), name='recipient-list'),
    path('recipient/<int:pk>/', views.RecipientRetrieveUpdateDestroyAPIView.as_view(), name='recipient-detail'),
    path('message/', views.MessageListCreateAPIView.as_view(), name='message-list'),
    path('message/<int:pk>/', views.MessageRetrieveUpdateDestroyAPIView.as_view(), name='message-detail'),
    path('sent-message/', views.SentMessageListCreateAPIView.as_view(), name='sent-message-list'),
    path('sent-message/<int:pk>/', views.SentMessageRetrieveUpdateDestroyAPIView.as_view(), name='sent-message-detail'),
]
