import socket
import argparse

def wake(args):
    IP = args.ip
    TOKEN = args.token
    target = (IP, 9302)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # get ps5 state
    payload = bytes.fromhex("53524348202a20485454502f312e310d0a6465766963652d646973636f766572792d70726f746f636f6c2d76657273696f6e3a30303033303031300d0a0d0a")

    s.sendto(payload,target)
    print(s.recv(1000))

    # wake up
    payload = bytes.fromhex("57414B455550202A20485454502F312E310A636C69656E742D747970653A76720A617574682D747970653A520A6D6F64656C3A25630A6170702D747970653A720A757365722D63726564656E7469616C3A25640A6465766963652D646973636F766572792D70726F746F636F6C2D76657273696F6E3A30303033303031300A00")
    payload = payload.replace(b"%c",b"w")
    payload = payload.replace(b"%d",TOKEN.encode())
    print(payload)

    s.sendto(payload,target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="udp boardcast ip")
    parser.add_argument("token", help="user token")
    args = parser.parse_args()
    wake(args)

