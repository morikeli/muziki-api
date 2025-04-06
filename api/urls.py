from api import views
from django.urls import path


urlpatterns = [
    path('', views.index_view, name='index'),
    path('messages/', views.load_message, name='messages'),
]
