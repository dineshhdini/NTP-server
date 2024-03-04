import socket
import ssl

def main():
    server_ip = input("Enter the server's IP address: ")
    server_address = (server_ip, 12345)

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection(server_address) as client_socket:
        with context.wrap_socket(client_socket, server_hostname=server_address[0]) as secure_client_socket:
            while True:
                timezone = input("Enter timezone (e.g., 'UTC', 'America/New_York') or type 'exit' to quit: ").strip()
                if timezone.lower() == 'exit':
                    break
                secure_client_socket.send(timezone.encode('utf-8'))
                response = secure_client_socket.recv(1024)
                print("Current time in", timezone, ":", response.decode('utf-8'))
if __name__ == "__main__":
    main()
