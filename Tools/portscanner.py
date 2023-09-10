import socket
import threading

def scan_port(target_host, port):
    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port} is open")

        sock.close()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        pass

def port_scanner(target_host, start_port, end_port):
    try:
        print(f"Scanning {target_host} for open ports...\n")

        for port in range(start_port, end_port + 1):

            thread = threading.Thread(target=scan_port, args=(target_host, port))
            thread.start()
    except KeyboardInterrupt:
        print("\nScan terminated.")


if __name__ == "__main__":
    target_host = input("Enter the target host or IP address: ")
    start_port = 1 
    end_port = int(input("Enter End port: "))  

    try:
        port_scanner(target_host, start_port, end_port)
    except KeyboardInterrupt:
        print("\nScan terminated.")
