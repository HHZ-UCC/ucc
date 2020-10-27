from django.urls import path

from . import views

urlpatterns = [
    path('bot/assign_alert', views.assign_alert, name='assign_alert'),
    path('bot/list_alerts', views.list_alerts, name='list_alerts')
]