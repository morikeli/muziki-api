from django.contrib import admin
from django.urls import path
from api.api import app

urlpatterns = [
    path('api/', app.urls),
    path('admin/', admin.site.urls),
]
