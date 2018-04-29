
from django.contrib import admin

from .models import TaxInfo, UserInfo, Federal, State

admin.site.register(TaxInfo)
admin.site.register(UserInfo)
admin.site.register(Federal)
admin.site.register(State)
