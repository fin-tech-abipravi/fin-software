from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AuthTFfield)
admin.site.register(UserField)
admin.site.register(AccessUsers)