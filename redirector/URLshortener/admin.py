from django.contrib import admin
from .models import URL, UserSavedLink

admin.site.register(URL)
admin.site.register(UserSavedLink)