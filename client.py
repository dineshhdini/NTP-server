import socket

def main():
    server_address = ('localhost', 12345)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            timezone = input("Enter timezone (e.g., 'UTC', 'America/New_York') or type 'exit' to quit: ").strip()
            if timezone.lower() == 'exit':
                break
            client_socket.sendto(timezone.encode('utf-8'), server_address)
            response, _ = client_socket.recvfrom(1024)
            print("Current time in", timezone, ":", response.decode('utf-8'))

if __name__ == "__main__":
    main()

