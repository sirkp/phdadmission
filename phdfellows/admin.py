from django.contrib import admin
from phdfellows.models import Application, WrittenTestScore
# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_filter = ['current_status']
    list_display = ['first_name','last_name','email','current_status']

admin.site.register(Application,ApplicationAdmin)
admin.site.register(WrittenTestScore)
