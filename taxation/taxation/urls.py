from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('brackets/', include('brackets.urls')),
    path('admin/', admin.site.urls),
]
