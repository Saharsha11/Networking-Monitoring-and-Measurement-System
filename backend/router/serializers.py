from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    router = serializers.DictField()
    system = serializers.DictField()
    network = serializers.DictField()
    wireless = serializers.DictField()
    dhcp = serializers.DictField()
    process = serializers.DictField()

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # =========================================================
        # ROUTER
        # =========================================================

        router = data.get("router", {})
        release = router.get("release", {})

        data["router"] = {
            "hostname": router.get("hostname"),
            "model": router.get("model"),
            "board": router.get("board_name"),
            "firmware": release.get("version"),
            "kernel": router.get("kernel"),
        }

        # =========================================================
        # SYSTEM
        # =========================================================

        system = data.get("system", {})
        memory = system.get("memory", {})

        total_memory = memory.get("total", 0)
        available_memory = memory.get("available", 0)

        memory_usage = 0

        if total_memory:
            memory_usage = round(
                ((total_memory - available_memory) / total_memory) * 100,
                2,
            )

        data["system"] = {
            "uptime": system.get("uptime"),
            "load": system.get("load", []),
            "memory": {
                "total": total_memory,
                "available": available_memory,
                "usage_percent": memory_usage,
            },
        }

        # =========================================================
        # NETWORK
        # =========================================================

        network = data.get("network", {})
        cleaned_network = {}

        for name, interface in network.items():
            stats = interface.get("stats", {})
            ipaddrs = interface.get("ipaddrs", [])
            link = interface.get("link", {})

            cleaned_network[name] = {
                "name": interface.get("name"),
                "type": interface.get("devtype"),
                "wireless": interface.get("wireless", False),
                "up": interface.get("up", False),

                "ip": (
                    ipaddrs[0].get("address")
                    if ipaddrs
                    else None
                ),

                "mac": interface.get("mac"),

                "rx_bytes": stats.get("rx_bytes", 0),
                "tx_bytes": stats.get("tx_bytes", 0),

                "rx_packets": stats.get("rx_packets", 0),
                "tx_packets": stats.get("tx_packets", 0),

                "rx_errors": stats.get("rx_errors", 0),
                "tx_errors": stats.get("tx_errors", 0),

                "rx_dropped": stats.get("rx_dropped", 0),
                "tx_dropped": stats.get("tx_dropped", 0),

                "carrier": link.get("carrier", False),
            }

        data["network"] = cleaned_network

        # =========================================================
        # WIRELESS
        # =========================================================

        wireless = data.get("wireless", {})
        cleaned_wireless = {}

        for radio_name, radio in wireless.items():

            config = radio.get("config", {})
            iwinfo = radio.get("iwinfo", {})

            interfaces = []

            for interface in radio.get("interfaces", []):
                interface_config = interface.get("config", {})
                interface_iwinfo = interface.get("iwinfo", {})

                interfaces.append({
                    "name": interface.get("ifname"),
                    "mode": interface_config.get("mode"),
                    "ssid": interface_config.get("ssid"),
                    "bssid": interface_config.get("bssid"),
                    "network": interface_config.get("network", []),

                    "wireless": {
                        "phy": interface_iwinfo.get("phy"),
                        "mode": interface_iwinfo.get("mode"),
                        "bssid": interface_iwinfo.get("bssid"),
                        "tx_power": interface_iwinfo.get("txpower"),
                        "country": interface_iwinfo.get("country"),
                        "hardware": interface_iwinfo.get(
                            "hardware", {}
                        ).get("name"),
                    },

                    "stations": interface.get("stations", []),
                })

            cleaned_wireless[radio_name] = {
                "up": radio.get("up", False),
                "disabled": radio.get("disabled", False),

                "band": config.get("band"),
                "channel": config.get("channel"),
                "htmode": config.get("htmode"),
                "country": config.get("country"),

                "hardware": iwinfo.get("hardware", {}).get("name"),
                "interfaces": interfaces,
            }

        data["wireless"] = cleaned_wireless

        # =========================================================
        # DHCP
        # =========================================================

        dhcp = data.get("dhcp", {})

        leases = dhcp.get("dhcp_leases", [])
        leases6 = dhcp.get("dhcp6_leases", [])

        data["dhcp"] = {
            "ipv4": leases,
            "ipv6": leases6,
            "total_ipv4": len(leases),
            "total_ipv6": len(leases6),
            "total_clients": len(leases) + len(leases6),
        }

        # =========================================================
        # PROCESSES
        # =========================================================

        process = data.get("process", {})

        if isinstance(process, dict):
            process_list = process.get("result", [])
        else:
            process_list = process

        cleaned_processes = []

        if isinstance(process_list, list):

            for process_item in process_list:
                cleaned_processes.append({
                    "pid": process_item.get("PID"),
                    "parent_pid": process_item.get("PPID"),
                    "user": process_item.get("USER"),
                    "state": process_item.get("STAT"),
                    "memory": process_item.get("%MEM"),
                    "cpu": process_item.get("%CPU"),
                    "command": process_item.get("COMMAND"),
                })

        data["process"] = {
            "total": len(cleaned_processes),
            "processes": cleaned_processes,
        }

        return data