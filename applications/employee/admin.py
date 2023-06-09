from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Branch)
admin.site.register(EntryHour)
admin.site.register(LunchEnd)
admin.site.register(LunchStart)
admin.site.register(ExitHour)