
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clearcache/', include('clearcache.urls')),
    path('', include('api.urls')),
    path('auth/', include('accounts.urls')),
    path('places/', include('places.urls')),
    path('closed/', include('closedcostumers.urls')),
    path('parties/', include('parties.urls')),
]

# urlpatterns += [
#     # match the root
#     ]
