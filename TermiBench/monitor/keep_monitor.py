import socket
from datetime import datetime
import threading
HOST = "0.0.0.0"
PORT = 7869

LOG_FILE = "received_logs.txt"

def write_log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def handle_connection(conn, addr):
    print(f"[+] Connection from {addr}")
    write_log(f"Connection established from {addr[0]}:{addr[1]}")
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode().strip()
                print(f"[{addr}] {message}")
                write_log(f"[{addr}] {message}")
            except Exception as e:
                print(f"[!] Error with {addr}: {e}")
                break
    print(f"[-] Disconnected: {addr}")
    write_log(f"Disconnected from {addr[0]}:{addr[1]}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[*] Listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_connection, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    main()