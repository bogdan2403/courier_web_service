from django.contrib import admin

# Register your models here.
from tracker.models import User, Place, Tracker

admin.site.register(User)
admin.site.register(Place)
admin.site.register(Tracker)