import socket
import time

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            continue
    return open_ports

if __name__ == "__main__":
    target = "127.0.0.1"
    ports = range(75, 85)
    result = scan_ports(target, ports)
    print(f"Open ports on {target}: {result}")
