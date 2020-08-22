from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Constituency)
admin.site.register(Constituency_category)
admin.site.register(Country)
admin.site.register(Parties)
admin.site.register(Politician_activities)
admin.site.register(Politician_education)
admin.site.register(Electoral_positions)
admin.site.register(Politicians)
admin.site.register(Regions)
admin.site.register(User_profile)
admin.site.register(Users)
admin.site.register(Politician_Category)
admin.site.register(Department)
admin.site.register(Tag)
admin.site.register(ElectionResult)
admin.site.register(District)

admin.site.site_header = "NBSUGVOTES2021"

