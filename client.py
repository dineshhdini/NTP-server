import socket
import pytz
from datetime import datetime

def send_request_to_server():
    # NTP server address and port
    server_address = '127.0.0.1'  # Replace with the IP address of your NTP server
    server_port = 12345  # Replace with the port number your NTP server is listening on

    # Prompt the user to enter a timezone
    timezone = input("Enter timezone (e.g., 'America/New_York'): ")

    # Validate the timezone
    try:
        pytz.timezone(timezone)
    except pytz.UnknownTimeZoneError:
        print("Invalid timezone!")
        return

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Send a request message to the server
        client_socket.sendto(timezone.encode(), (server_address, server_port))

        # Receive the response from the server
        response, server = client_socket.recvfrom(1024)
        print("Response from server:", response.decode())

if __name__ == "__main__":
    send_request_to_server()
