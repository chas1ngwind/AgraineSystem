from django.contrib import admin
#from Seed.models import SeedInfo, DetailInfo, GenerationInfo, RoleInfo
# Register your models here.
from Seed.models import DetailInfo, RoleInfo


class DetailInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'role', 'type', 'generation', 'amount', 'name', 'contactnumber']


class RoleInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'role']


admin.site.register(RoleInfo, RoleInfoAdmin)

admin.site.register(DetailInfo, DetailInfoAdmin)
