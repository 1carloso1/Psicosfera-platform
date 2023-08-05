from django.contrib import admin
from django.urls import path, include
from home.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name = 'home'),
    path('login/', include('login.urls')),
]
