from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Constituency)
admin.site.register(Constituency_category)
admin.site.register(Country)
admin.site.register(Groups)
admin.site.register(Parties)
admin.site.register(Permissions)
admin.site.register(Permissions_map)
admin.site.register(Politician_activities)
admin.site.register(Politician_education)
admin.site.register(Politicians)
admin.site.register(Regions)
admin.site.register(Systemlogs)
admin.site.register(User_permissions)
admin.site.register(User_profile)
admin.site.register(Users)
admin.site.register(Politician_Category)
admin.site.register(Users_session)
admin.site.register(Department)
admin.site.register(Tag)

