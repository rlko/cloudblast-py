import os
from typing import Dict, Optional, List
import requests


class CloudBlastError(Exception):
    """Base exception for CloudBlast API errors."""
    def __init__(
            self,
            message: str,
            response: Optional[requests.Response] = None
    ):
        self.message = message
        self.response = response
        if response is not None:
            try:
                self.error_details = response.json()
            except ValueError:
                self.error_details = response.text
        else:
            self.error_details = None
        super().__init__(self.message)

    def __str__(self):
        if self.error_details:
            return f"{self.message}\nError details: {self.error_details}"
        return self.message


class CloudBlast:
    """CloudBlast API client."""

    BASE_URL = "https://console.cloudblast.io/api/public"

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the CloudBlast client.

        Args:
            api_key: Your CloudBlast API key.
                If not provided, will try to get from
                CLOUDBLAST_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("CLOUDBLAST_API_KEY")
        if not self.api_key:
            raise CloudBlastError(
                "API key is required. "
                "Set it via constructor or "
                "CLOUDBLAST_API_KEY environment variable."
            )

        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """Make a request to the CloudBlast API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            **kwargs: Additional arguments to pass to requests

        Returns:
            Dict containing the API response

        Raises:
            CloudBlastError: If the API request fails
        """
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"

        # Add authKey to the request body if it's a POST request
        if method == "POST" and "json" in kwargs:
            kwargs["json"]["authKey"] = self.api_key

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise CloudBlastError(
                f"API request failed: {str(e)}",
                response=e.response
            )
        except requests.exceptions.RequestException as e:
            raise CloudBlastError(f"API request failed: {str(e)}")

    def create_server(
        self,
        plan_id: int,
        location_id: int,
        hostname: str,
        template_uuid: str,
        **kwargs
    ) -> Dict:
        """Create a new server.

        Args:
            plan_id: ID of the plan to use
            location_id: ID of the location to deploy in
            hostname: Hostname for the server
            template_uuid: UUID of the template to use
            **kwargs: Additional parameters to pass to the API

        Returns:
            Dict containing the server details

        Raises:
            CloudBlastError: If the server creation fails
        """
        data = {
            "plan_id": plan_id,
            "location_id": location_id,
            "hostname": hostname,
            "template_uuid": template_uuid,
            **kwargs
        }

        return self._request("POST", "/create-server", json=data)

    def send_action_server(self, server_id: int, action: str) -> Dict:
        """Send an action to a server.

        Args:
            server_id: ID of the server
            action: Action to perform (e.g., 'start', 'stop', 'restart')

        Returns:
            Dict containing the action result

        Raises:
            CloudBlastError: If the action fails
        """
        data = {
            "server_id": server_id,
            "action": action
        }
        return self._request("POST", "/send-action-server", json=data)

    def delete_server(self, server_id: int) -> Dict:
        """Delete a server.

        Args:
            server_id: ID of the server to delete

        Returns:
            Dict containing the deletion result

        Raises:
            CloudBlastError: If the deletion fails
        """
        return self._request(
            "POST",
            "/delete-server",
            json={"server_id": server_id}
        )

    def add_extra_ip(self, server_id: int) -> Dict:
        """Add an extra IP to a server.

        Args:
            server_id: ID of the server

        Returns:
            Dict containing the IP addition result

        Raises:
            CloudBlastError: If the IP addition fails
        """
        return self._request(
            "POST",
            "/add-extra-ip",
            json={"server_id": server_id}
        )

    def remove_extra_ip(self, server_id: int, ip_address: str) -> Dict:
        """Remove an extra IP from a server.

        Args:
            server_id: ID of the server
            ip_address: IP address to remove

        Returns:
            Dict containing the IP removal result

        Raises:
            CloudBlastError: If the IP removal fails
        """
        data = {
            "server_id": server_id,
            "ip_address": ip_address
        }
        return self._request("POST", "/remove-extra-ip", json=data)

    def get_server_details(self, server_id: int) -> Dict:
        """Get details of a specific server.

        Args:
            server_id: ID of the server

        Returns:
            Dict containing the server details

        Raises:
            CloudBlastError: If the request fails
        """
        return self._request("GET", f"/servers/details/{server_id}")

    def list_servers(self) -> List[Dict]:
        """Get a list of all servers.

        Returns:
            List of Dicts containing server details

        Raises:
            CloudBlastError: If the request fails
        """
        return self._request("GET", "/servers/all")
