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
    try:
        # Attempt to decode the data as UTF-8
        country = data.decode('utf-8')
    except UnicodeDecodeError:
        # If decoding as UTF-8 fails, try decoding with a different encoding or ignore errors
        country = data.decode('latin-1', errors='ignore')  # Example: decoding with Latin-1 and ignoring errors

    # Continue with the rest of the function...


def send_time_response(response, client_address):
    # Send time response back to client over SSL
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('10.20.204.17', 12345))
        server_socket.listen(5)
        conn, addr = server_socket.accept()

        # Wrap the connection with SSL
        ssl_socket = ssl.wrap_socket(conn, server_side=True, certfile="server.crt", keyfile="server.key")

        # Send the response
        ssl_socket.send(response)

        # Close the SSL connection
        ssl_socket.close()

def main():
    global running
    # Set up TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('10.20.204.17', 12345))
        server_socket.listen(5)

        # Load SSL certificate and key
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile="server.crt", keyfile="server.key")

        print("NTP server started...")

        while running:
            # Accept client connections
            conn, addr = server_socket.accept()
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

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_server()
