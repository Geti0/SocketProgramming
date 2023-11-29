import socket

def main():
    serverName = 'localhost'
    serverPort = 1200
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((serverName, serverPort))
        print("Jeni lidhur me serverin.")

    except Exception as e:
        print(f"Gabim gjate lidhjes me serverin: {e}")

    finally:
        s.close()

if __name__ == "__main__":
    main()