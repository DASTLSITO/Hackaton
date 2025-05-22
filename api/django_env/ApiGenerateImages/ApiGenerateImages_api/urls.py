# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from ApiGenerateImages_api import urls as generate_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(generate_urls)),
    path('generateImg', generate_urls.as_view())
]