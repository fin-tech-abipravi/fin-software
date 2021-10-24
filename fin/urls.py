
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clearcache/', include('clearcache.urls')),
    path('',include('api.urls')),
    path('auth/', include('accounts.urls')),
]

# urlpatterns += [
#     # match the root
#     ]