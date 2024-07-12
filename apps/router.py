from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.users.urls')),
    path('addresses/', include('apps.addresses.urls')),
    path('apartments/', include('apps.apartments.urls')),
    # path('reservations/', include('apps.reservations.urls')),
]
