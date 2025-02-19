import socket
import docker

def scan_ports(ip):
    open_ports = []
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def identify_docker_sockets(open_ports):
    docker_sockets = []
    client = docker.from_env()
    for port in open_ports:
        try:
            client.ping()
            docker_sockets.append(port)
        except docker.errors.APIError:
            continue
    return docker_sockets

if __name__ == "__main__":
    ip = "127.0.0.1"  # Change this to the target IP address
    open_ports = scan_ports(ip)
    print(f"Open ports: {open_ports}")
    docker_sockets = identify_docker_sockets(open_ports)
    print(f"Docker sockets: {docker_sockets}")
