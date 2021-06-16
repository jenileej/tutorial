from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # first segment of url to be
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
