# NTP Client

## Description
This project implements a simple NTP (Network Time Protocol) client in Python. The client queries an NTP server to synchronize its time with the server's time. This can be useful for applications that require accurate and synchronized time information.

## Features
- Queries an NTP server to get the current time
- Parses the NTP response to calculate the current time
- Handles socket communication with the NTP server
- Displays the current time obtained from the NTP server

## Usage
1. Clone the repository:
2. Navigate to the project directory:
3. Run the NTP client:
4. The client will output the current time obtained from the NTP server.

## Configuration
- By default, the client queries the `pool.ntp.org` NTP server. You can change the server address in the `get_ntp_time` function in the `ntp_client.py` file.
- The client uses UDP port 123 to communicate with the NTP server. Ensure that your firewall allows outbound UDP traffic on this port.

## Dependencies
- Python 3.x

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
