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

def get_dashboard_data():
    client = get_ubus_client()

    router = client.call("system","board")
    system = client.call("system", "info")
    network = client.call("luci-rpc", "getNetworkDevices")
    wireless = client.call("luci-rpc", "getWirelessDevices")
    dhcp = client.call("luci-rpc", "getDHCPLeases")
    process = client.call("luci","getProcessList")

    return {
        "router":router["result"][1],
        "system": system["result"][1],
        "network": network["result"][1],
        "wireless": wireless["result"][1],
        "dhcp": dhcp["result"][1],
        "process":process["result"][1]
    }