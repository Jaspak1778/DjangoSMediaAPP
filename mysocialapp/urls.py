#mysocialapp urls
from django.contrib import admin
from django.urls import path, include
#reitti main apin urleihin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.ulrs'))
]


#ok