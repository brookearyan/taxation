from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('brackets/', include('brackets.urls')),
        path('admin/', admin.site.urls),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
