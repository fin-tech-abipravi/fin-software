from django.contrib import admin
from . models import Costumerdetails, Collectionlist, Dlammounts, Ammountinhand, Expence, Expencetotal, Closeup, Closedown, Otherammountin, Otherammountout, Inversment, Others
# Register your models here.
admin.site.register(Costumerdetails)
admin.site.register(Collectionlist)
admin.site.register(Dlammounts)
admin.site.register(Ammountinhand)
admin.site.register(Expence)
admin.site.register(Expencetotal)
admin.site.register(Closeup)
admin.site.register(Closedown)
admin.site.register(Otherammountin)
admin.site.register(Otherammountout)
admin.site.register(Inversment)
admin.site.register(Others)