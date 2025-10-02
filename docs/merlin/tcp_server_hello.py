import socket

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345      # Port to listen on (use a port > 1024 if not running as root)

def start_server():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)  # Listen for incoming connections (backlog = 1)

        print(f"Server listening on {HOST}:{PORT}...")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connection from {client_address}")
                client_socket.sendall(b'Hello')  # Send a simple "Hello" message
                print("Sent 'Hello' to client")
                # Close the connection (will happen automatically with `with` block)

if __name__ == '__main__':
    start_server()


