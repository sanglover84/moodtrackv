from django.contrib import admin
from .models import MedsPost

class MedsPostAdmin(admin.ModelAdmin):
    list_display = (
        "generic",
        "totaldose",
        "dose1",
        "dose2",
        "dose3",
        "frequency",
        "type",
        "whatfor",
        "sideeffects",
    )

# Register your models here.
admin.site.register(MedsPost,MedsPostAdmin)