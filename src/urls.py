from django.contrib import admin
from django.urls import path, include
from api.api import app


urlpatterns = [
    path('api/', app.urls),
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
]
