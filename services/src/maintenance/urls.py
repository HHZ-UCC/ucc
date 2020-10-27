from django.urls import path

from . import views

urlpatterns = [
    path('bot/assign_ticket', views.assign_ticket, name='assign_ticket'),
    path('bot/list_tickets', views.list_tickets, name='list_tickets')
]