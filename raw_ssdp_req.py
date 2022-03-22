import socket

src_ip = "192.168.1.44" # the IP of the interface/adapter you're sending from
dst_ip = "239.255.255.250" # this is known as the multicast address. 
src_port = 62950 # random source port who cares
dst_port = 1900 # destination port
buffer_size = 1024 # buffer size to receive using UDP server

addr = (dst_ip, dst_port) # tuple containing destination ip and port we're sending to

# SSDP uses UDP, so we use socket.SOCK_DGRAM as the socket type
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((src_ip, src_port)) # use particular interface from IP

body = ( # request content, like HTTP
'M-SEARCH * HTTP/1.1\r\n' + # title. we're searching for Upnp devices, not advertising
'ST: ssdp:all\r\n' + # ssdp:all means ALL Upnp devices, no categories (search targets)
'MX: 3\r\n' + # max amount of seconds a receiving device has to respond
'MAN: "ssdp:discover"\r\n' + # message type. always ssdp:discover for M-SEARCH
f'HOST: {dst_ip}:{dst_port}\r\n\r\n' # the host and port that the discovery message will be sent to
).encode("utf-8") # encode the request body into UTF-8 bytes

# unlike TCP, UDP does not use sessions, so you just send the IP packet and hope it arrives at its destination
sock.sendto(body, addr) # send content (body) to particular address

while(True): # keep waiting to receive messages on port src_port that we binded to
    c_body_raw, c_addr = sock.recvfrom(1024) # client body and client address
    c_body = c_body_raw.decode('utf-8') 
    print(f"Message from {c_addr}:")
    print(c_body)