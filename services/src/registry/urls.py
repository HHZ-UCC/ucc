from django.urls import path

from . import views

urlpatterns = [
    path('bot/action', views.bot_action, name='bot_action'),
    path('', views.get_registry_info, name='get_registry_info'),
    # path('test', views.test, name='test'),
]