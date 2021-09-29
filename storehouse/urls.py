from django.contrib import admin
from django.urls import path, include
from frontend.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-api/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
    path('', index),
]