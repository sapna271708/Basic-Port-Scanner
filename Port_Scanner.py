import socket

# Target IP or website
target = input("Enter IP Address or Website: ")

print(f"\nScanning target: {target}")
print("Open Ports:\n")

# Scan ports from 1 to 100
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("\nScanning Completed!")