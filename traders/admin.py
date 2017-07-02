from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from traders.models import Trader

admin.site.register(Trader, UserAdmin)
