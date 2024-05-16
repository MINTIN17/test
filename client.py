import socket
import threading

# Khởi tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Xác định host và cổng của server
host = '127.0.0.1'
port = 12346

# Kết nối đến server
client_socket.connect((host, port))

# Nhập tên người dùng
username = input("Nhập tên người dùng: ")
client_socket.send(username.encode('utf-8'))

# Xử lý nhận và gửi tin nhắn
def receive_messages():
    while True:
        try:
            # Nhận tin nhắn từ server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Lỗi: {e}")
            client_socket.close()
            break

# Thread nhận tin nhắn từ server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Gửi tin nhắn đến người dùng khác
while True:
    recipient = input("Nhập tên người dùng bạn muốn nhắn tin: ")
    message = input("Nhập tin nhắn của bạn: ")
    client_socket.send(f"@{recipient} {message}".encode('utf-8'))
