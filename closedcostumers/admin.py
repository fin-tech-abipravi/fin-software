from django.contrib import admin
from .models import *
# Register your models here.
models = [Costumers, Loandetails]

for x in models:
    admin.site.register(x)
