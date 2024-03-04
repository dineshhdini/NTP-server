import socket
import ssl
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
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Try to bind to an available port
        for port in range(12345, 12445):  # Try ports 12345 to 12444
            try:
                server_socket.bind(('0.0.0.0', 12345))
                server_socket.listen(5)
                conn, addr = server_socket.accept()
                ssl_socket = ssl.wrap_socket(conn, certfile="server.crt", keyfile="server.key", server_side=True)
                ssl_socket.send(response)
                ssl_socket.close()
                break  # Exit the loop if binding is successful
            except OSError as e:
                if e.errno == 10048:  # Address already in use
                    continue  # Try the next port
                else:
                    raise  # Re-raise other OSError exceptions

def main():
    global running
    # Set up TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Load SSL certificate and key
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile="C:\\Users\\HP\\Desktop\\CN Project\\server.crt", keyfile="C:\\Users\\HP\\Desktop\\CN Project\\server.key")
        
        # Wrap socket with SSL
        ssl_socket = ssl_context.wrap_socket(server_socket, server_side=True)
        ssl_socket.bind(('0.0.0.0', 12345))
        ssl_socket.listen(5)
        print("NTP server started...")

        while running:
            # Accept client connections
            conn, addr = ssl_socket.accept()
            print("Accepted connection from:", addr)

            # Receive request from client
            data = conn.recv(1024)
            print("Received request from:", addr)

            # Handle client request in a separate thread
            client_thread = threading.Thread(target=handle_client_request, args=(data, addr))
            client_thread.start()


def stop_server():
    global running
    print("Stopping server...")
    running = False

if _name_ == "_main_":
    try:
        main()
    except KeyboardInterrupt:
        stop_server()
