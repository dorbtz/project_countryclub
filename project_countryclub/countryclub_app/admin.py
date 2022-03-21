from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(ClubModel),
admin.site.register(Club),
# admin.site.register(ClubStaff),
admin.site.register(ClubMembers),

