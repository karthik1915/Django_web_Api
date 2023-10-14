from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
]
