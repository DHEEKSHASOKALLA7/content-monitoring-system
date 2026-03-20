from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('monitor.urls')),  # 🔥 THIS LINE IS THE KEY
]