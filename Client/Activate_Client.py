import socket

def run_client():

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ("localhost", 5000)
    client_socket.connect(server_address)

    try:
        user_message = ""
        while (user_message.lower() != "quit"):

            # Get user input
            # TODO this part show somehow connect to the user interface triggers/events
            user_message = input("Enter a message to send to the server:\n").lower().strip()

            # Send message to server
            client_socket.sendall(user_message.encode())
            
        else:
            print("Client disconnected, goodbye!")
            
    
    except:
        ("Client >  ERROR whilst attempting server connection")
    finally:
        client_socket.close()



if __name__ == "__main__":
    run_client()
