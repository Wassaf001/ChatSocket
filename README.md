# Simple Chat Application

This is a simple chat application implemented in Python using socket programming. The application includes one server and three clients (client, client1, client2) that can communicate in real-time.

## Features
- **Client-Server Architecture**: Real-time chat using Python sockets.
- **Concurrent Connections**: Supports multiple clients with multi-threading.
- **Simple User Interface**: Basic interface for sending and receiving messages.

## Requirements
- Python 3.x

## Installation
1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/yourusername/chat-app.git
    cd chat-app
    ```

2. Ensure you have Python 3 installed. You can check your Python version using:
    ```sh
    python --version
    ```

## Usage

### Running the Server
1. Navigate to the project directory.
2. Run the server script:
    ```sh
    python3 server.py
    ```

### Running the Clients
1. Open three separate terminal windows or tabs.
2. In each terminal, navigate to the project directory and run a client script:
    ```sh
    python3 client.py
    ```
    ```sh
    python3 client1.py
    ```
    ```sh
    python3 client2.py
    ```

### Interaction
- Type a message in any client terminal and press Enter to send it.
- Messages will be broadcasted to all connected clients, and each client will display incoming messages from others.

## File Structure
- `server.py`: The server script that handles client connections and message broadcasting.
- `client.py`: The first client script for sending and receiving messages.
- `client1.py`: The second client script for sending and receiving messages.
- `client2.py`: The third client script for sending and receiving messages.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Contact
For any inquiries, please contact [Wassaf](mailto:wassafali213@gmail.com).

