import socket
import threading
import pytz
from datetime import datetime

# Global variable to track whether the server should continue running
running = True

def main_ntp_server_request():
    # Main NTP server details
    main_ntp_server = 'pool.ntp.org'  # You can use any NTP server here
    main_ntp_port = 123  # NTP port
    
    # Craft an NTP request packet (NTP version 4)
    ntp_request_packet = bytearray(48)
    ntp_request_packet[0] = 0x1B  # NTP control message header (version 4, mode 3 for client)

    # Send the request and receive response
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.settimeout(5)  # Timeout in seconds
        try:
            client_socket.sendto(ntp_request_packet, (main_ntp_server, main_ntp_port))
            ntp_response_packet, server_address = client_socket.recvfrom(1024)
            return ntp_response_packet
        except socket.timeout:
            print("Timeout: Unable to get response from the main NTP server.")
            return None

def handle_client_request(data, client_address):
    global running
    # Extract timezone information from client request
    timezone = data.decode('utf-8')

    # Get current time in the specified timezone
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        time_str = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
        response = time_str.encode('utf-8')
    except pytz.UnknownTimeZoneError:
        response = b'Invalid timezone'
    
    # Send time response back to client
    send_time_response(response, client_address)
    
    # Check if the server should continue running
    if not running:
        stop_server()

def send_time_response(response, client_address):
    # Send time response back to client
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.sendto(response, client_address)

def main():
    global running
    # Set up UDP socket
    host = '0.0.0.0'
    port = 12345  # Choose any available port
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print("NTP server started...")

        while running:
            # Receive request from client
            data, client_address = server_socket.recvfrom(1024)
            print("Received request from:", client_address)

            # Handle client request in a separate thread
            client_thread = threading.Thread(target=handle_client_request, args=(data, client_address))
            client_thread.start()

def stop_server():
    global running
    print("Stopping server...")
    running = False

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_server()
