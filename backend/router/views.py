from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from .services import(
    get_network_devices,
    get_dhcp_leases,
    get_system_info,
    get_wireless_devices,
    get_process_list,get_dashboard_data
)

# Create your views here.
class RouterSystemView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        data = get_system_info()
        return Response(data)

class RouterNetworkView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        data = get_network_devices()
        return Response(data , status= status.HTTP_200_OK)

class RouterProcessView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        data = get_process_list()
        return Response( data , status=status.HTTP_200_OK)

class RouterDHCPView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        data = get_dhcp_leases()
        return Response(data , status=status.HTTP_200_OK)

class RouterWirelessView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        data = get_wireless_devices()
        return Response(data , status=status.HTTP_200_OK)

class RouterDashboardView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        data = get_dashboard_data()
        return Response(data)
