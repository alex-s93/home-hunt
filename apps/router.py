from django.urls import path, include

urlpatterns = [
    path('', include('apps.users.urls')),
    # path('reservations/', include('apps.reservations.urls')),
]
