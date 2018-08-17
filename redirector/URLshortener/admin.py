from django.contrib import admin
from .models import URL, SavedLink

admin.site.register(URL)
admin.site.register(SavedLink)