import socket

def main():
    serverName = '127.0.0.1'
    serverPort = 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((serverName, serverPort))
        print("Jeni lidhur me serverin.")

        username = "getuar"
        password = "123"

        auth_request = f"AUTHENTICATE:{username}:{password}"
        auth_response = send_request_to_server(s, auth_request)
        print(auth_response)

    except Exception as e:
        print(f"Gabim gjate lidhjes me serverin: {e}")

    finally:
        s.close()

if __name__ == "__main__":
    main()