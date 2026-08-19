import requests

class UbusClient:
    def __init__(self, router_url, username, password):
        self.router_url = router_url
        self.username = username
        self.password = password

        self.session_id = None

    def login(self):
        """
        Login to OpenWrt Ubus and obtain a Ubus session ID.
        """

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "call",
            "params": [
                "0" * 32,
                "session",
                "login",
                {
                    "username": self.username,
                    "password": self.password,
                    "timeout": 3600,
                },
            ],
        }

        response = requests.post(
            self.router_url,
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if "error" in data:
            raise Exception(
                f"Ubus login failed: {data['error']}"
            )

        try:
            self.session_id = data["result"][1]["ubus_rpc_session"]
            print(self.session_id)
        except (KeyError, IndexError, TypeError):
            raise Exception(
                f"Could not obtain Ubus session ID: {data}"
            )

        return self.session_id

    def call(self, object_name, method, params=None):
        """
        Call an OpenWrt Ubus method using the current session.
        """

        if not self.session_id:
            self.login()

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "call",
            "params": [
                self.session_id,
                object_name,
                method,
                params or {},
            ],
        }

        response = requests.post(
            self.router_url,
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        # Ubus error
        if "error" in data:
            error = data["error"]

            # Session expired / invalid
            if error.get("code") == -32002:
                self.session_id = None

                # Login again and retry once
                self.login()

                return self.call(
                    object_name,
                    method,
                    params,
                )

            raise Exception(
                f"Ubus call failed: {error}"
            )

        return data