from django.conf import settings

from .ubus import UbusClient


def get_ubus_client():
    return UbusClient(
        router_url=settings.OPENWRT_UBUS_URL,
        username=settings.OPENWRT_USERNAME,
        password=settings.OPENWRT_PASSWORD,
    )

def get_system_info():
    client = get_ubus_client()

    return client.call(
        "system",
        "info",
    )


def get_network_devices():
    client = get_ubus_client()

    return client.call(
        "luci-rpc",
        "getNetworkDevices",
    )


def get_wireless_devices():
    client = get_ubus_client()

    return client.call(
        "luci-rpc",
        "getWirelessDevices",
    )


def get_dhcp_leases():
    client = get_ubus_client()

    return client.call(
        "luci-rpc",
        "getDHCPLeases",
    )


def get_process_list():
    client = get_ubus_client()

    return client.call(
        "luci",
        "getProcessList",
    )