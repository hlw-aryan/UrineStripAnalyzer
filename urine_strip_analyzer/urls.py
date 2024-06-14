from django.urls import path, include
from django.contrib import admin
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('analyzer.urls')),
    path('', index, name='index'),
]