import socket     # For network communication
import threading  # For creating threads


def handle_client(connection, client_address):
    """
    This function is used to process communication with an 
    individual client.

    params: 
    connection - the socket object repressenting the client connection
    client_address - a tuple containing the client's IP address and port.
    """

    try:
        print(f"[SERVER] Connection established with client {client_address}")

        while True:
            # Receive data from client
            data = connection.recv(1024)

            # If data received is empty break (sign of client termination)
            if not data: 
                break

            print(f"[SERVER] Received data from {client_address}: {data.decode()}")

    finally:
        connection.close()

    
    
def run_server():

    # Create a server socket 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ("localhost", 5000)
    server_socket.bind(server_address)

    # Listen for incoming client
    server_socket.listen(5)

    print(f"[SERVER] Server is activate and listening for incoming client connections on port {server_address[1]} ...")

    try:
        while True:
            # Accept a connection
            connection, client_address = server_socket.accept()

            # Create a new thread to handle the client
            client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
            client_thread.start()

    except:
        ("[SERVER] ERROR whilst attempting client connection")

    finally:
        server_socket.close()


if __name__ == "__main__":
    run_server()

