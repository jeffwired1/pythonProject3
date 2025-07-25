import socket
import datetime


def get_nist_time():
    # NIST time server address and port
    host = 'time.nist.gov'
    port = 37

    # Connect to the NIST time server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Receive 4 bytes of time data from the server
    raw_time = client.recv(4)
    client.close()

    # Convert the raw time data to an integer (NTP timestamp)
    timestamp = int.from_bytes(raw_time, 'big')

    # Calculate the Unix timestamp (subtract 2,208,988,800, which is the difference between NTP and Unix epochs)
    unix_timestamp = timestamp - 2208988800

    # Convert the Unix timestamp to a datetime object
    nist_time = datetime.datetime.utcfromtimestamp(unix_timestamp)

    return nist_time


# Get the current time from NIST and print it
current_time = get_nist_time()
print("Current time from NIST:", current_time)

