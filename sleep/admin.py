from django.contrib import admin
from .models import Sleep

# Register your models here.

class SleepAdmin(admin.ModelAdmin):
    list_display = (
        "datetime",
        "author",
        "hourssleep",
        "notes",
    )

admin.site.register(Sleep, SleepAdmin)
