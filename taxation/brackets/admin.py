
from django.contrib import admin

from .models import UserInfo, Federal, State

admin.site.register(UserInfo)
admin.site.register(Federal)
admin.site.register(State)
