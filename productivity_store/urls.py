# productivity_store/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gadgets/', include('gadgets.urls')),
    path('', include('gadgets.urls')),
    
]
