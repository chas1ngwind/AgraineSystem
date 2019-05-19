from django.contrib import admin
#from Seed.models import SeedInfo, DetailInfo, GenerationInfo, RoleInfo
# Register your models here.
from Seed.models import DetailInfo, RoleInfo

# class DetailInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'role', 'type', 'generation', 'amount']
#
# class SeedInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'selectRole', 'type']
#
# class GenerationInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'role1', 'type1', 'generation']
# class RoleInfoAdmin(admin.ModelAdmin):
#     list_display = ['id', 'role']
#
# #register SeedInfo
# admin.site.register(SeedInfo, SeedInfoAdmin)
# #register GenerationInfo
# admin.site.register(GenerationInfo, GenerationInfoAdmin)
# #register RoleInfo
# admin.site.register(RoleInfo, RoleInfoAdmin)
# #register DetailInfo
# admin.site.register(DetailInfo, DetailInfoAdmin)


class DetailInfoAdmin(admin.ModelAdmin):
     list_display = ['id', 'role', 'type', 'generation', 'amount']


class RoleInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'role']


admin.site.register(RoleInfo, RoleInfoAdmin)

admin.site.register(DetailInfo, DetailInfoAdmin)