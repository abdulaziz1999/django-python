from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)


@admin.register(Students)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['f_name', 'l_name', 'email']
    # exclude = ('id',)
