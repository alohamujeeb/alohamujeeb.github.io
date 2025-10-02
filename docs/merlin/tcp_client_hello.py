import socket

HOST = '127.0.0.1'  # Server IP address
PORT = 12345        # Server port

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        # Receive the server's message
        data = client_socket.recv(1024)
        print("Received from server:", data.decode())

        # Send a line back to the server
        message = "Thanks, server!"
        client_socket.sendall(message.encode())
        print("Sent to server:", message)

if __name__ == '__main__':
    start_client()


