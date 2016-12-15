from django.contrib import admin
from collection.models import Thing, Social, Team

# Register your models here.
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'user', 'description', 'team')
    prepopulated_fields = {'slug': ('name',)}

class SocialAdmin(admin.ModelAdmin):
    model = Social
    list_display = ['network', 'username',]

class TeamAdmin(admin.ModelAdmin):
    model = Team
    list_display = ['name',]

admin.site.register(Thing, ThingAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Team, TeamAdmin)
