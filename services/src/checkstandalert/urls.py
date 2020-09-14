from django.urls import path

from . import views

urlpatterns = [
    path('bot/action', views.bot_action, name='bot_action'),
    # path('test', views.test, name='test'),
]