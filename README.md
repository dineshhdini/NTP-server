<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NTP Client README</title>
</head>
<body>
    <h1>NTP Client</h1>

    <h2>Description</h2>
    <p>This project implements a simple NTP (Network Time Protocol) client in Python. The client queries an NTP server to synchronize its time with the server's time. This can be useful for applications that require accurate and synchronized time information.</p>

    <h2>Features</h2>
    <ul>
        <li>Queries an NTP server to get the current time</li>
        <li>Parses the NTP response to calculate the current time</li>
        <li>Handles socket communication with the NTP server</li>
        <li>Displays the current time obtained from the NTP server</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li>Clone the repository:</li>
        <code>git clone https://github.com/your-username/ntp-client.git</code>
        <li>Navigate to the project directory:</li>
        <code>cd ntp-client</code>
        <li>Run the NTP client:</li>
        <code>python ntp_client.py</code>
        <li>The client will output the current time obtained from the NTP server.</li>
    </ol>

    <h2>Configuration</h2>
    <ul>
        <li>By default, the client queries the <code>pool.ntp.org</code> NTP server. You can change the server address in the <code>get_ntp_time</code> function in the <code>ntp_client.py</code> file.</li>
        <li>The client uses UDP port 123 to communicate with the NTP server. Ensure that your firewall allows outbound UDP traffic on this port.</li>
    </ul>

    <h2>Dependencies</h2>
    <ul>
        <li>Python 3.x</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
