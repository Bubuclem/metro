from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('metro.urls')),
    path('admin/', admin.site.urls),
]
