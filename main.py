import socket
import requests

GOOGLE_DNS_SERVER = "8.8.8.8"
IPIFY_API_URL = "https://api.ipify.org"

# Invalid IP address for testing get_private_ip() function error handling.
# GOOGLE_DNS_SERVER = "invalid_ip_address"

# URL for testing get_public_ip() function error handling.
# IPIFY_API_URL = "https://httpbin.org/status/404"

def get_private_ip():
    """
    Retrieves the device's private IPv4 address.

    Opens a temporary UDP socket connection to an external address to determine your private IPv4 address.
    No data packets are sent.

    Returns:
        str: The private IPv4 address. None: If it fails.
    """     
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
            my_socket.connect((GOOGLE_DNS_SERVER, 53))
            return my_socket.getsockname()[0]
    except Exception as error_message:
        print(f"Error retrieving PRIVATE IP: {error_message}")
        return None

def get_public_ip():
    """
    Retrieves the network's public IPv4 address.

    Sends a GET request to the ipify API to obtain your public IPv4 address.

    Returns:
        str: The public IPv4 address. None: If it fails.
    """
    try:
        response = requests.get(IPIFY_API_URL, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        else:
            print(f"Error retrieving PUBLIC IP, status code: {response.status_code}")
            return None
    except requests.RequestException as error_message:
        print(f"Error retrieving PUBLIC IP.: {error_message}")
        return None

if __name__ == "__main__":
    private_ip = get_private_ip()
    public_ip = get_public_ip()

    print(f"Private IP: {private_ip if private_ip else 'unavailable'}")
    print(f"Public IP.: {public_ip if public_ip else 'unavailable'}")
