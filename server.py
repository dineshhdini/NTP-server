import socket
import threading
import pytz
from datetime import datetime

# Global variable to track whether the server should continue running
running = True

# Dictionary mapping country names to their respective timezones
country_timezones = {
    'USA': 'America/New_York',
    'UK': 'Europe/London',
    'India': 'Asia/Kolkata',
    'Japan': 'Asia/Tokyo',
    # Add more countries and their timezones as needed
}

def handle_client_request(data, client_address):
    global running
    # Extract country name from client request
    country = data.decode('utf-8')

    # Get timezone for the specified country
    timezone = country_timezones.get(country)

    if timezone:
        # Get current time in the specified timezone
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            time_str = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')
            response = time_str.encode('utf-8')
        except pytz.UnknownTimeZoneError:
            response = b'Invalid timezone'
    else:
        response = b'Country not found'

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
