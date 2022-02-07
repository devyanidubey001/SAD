from django.contrib import admin
from teammate.models import Teammate
# Register your models here.
class TeammateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'first_name', 'last_name')
admin.site.register(Teammate,TeammateAdmin)
