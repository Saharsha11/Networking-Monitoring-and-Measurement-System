from django.urls import path
from .views import (
    RouterDHCPView,
    RouterNetworkView,
    RouterProcessView,
    RouterSystemView,
    RouterWirelessView
)

urlpatterns = [
    path('dhcp/',RouterDHCPView.as_view(),name="dhcp"),
    path('network/',RouterNetworkView.as_view(),name="network"),
    path('process/',RouterProcessView.as_view(),name="process"),
    path('system/',RouterSystemView.as_view(),name="system"),
    path('wireless/',RouterWirelessView.as_view(),name="wireless"),
]
