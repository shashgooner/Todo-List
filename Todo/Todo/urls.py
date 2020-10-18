from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoApi/', include('todoApi.urls')),
    path('account/', include('account.urls')),
]