import requests as rq
import socks

s = socks.socksocket()
s.setproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050)
s.connect(('ipinfo.io', 80))
s.send(b'GET / HTTP/1.1\r\nHost:ipinfo.io\r\n\r\n')
data = ''
buf = s.recv(1024)
while len(buf):
    data += buf.decode()
    print(data)
    buf = s.recv(1024)
s.close()

print("Connected from %s." % data)

proxies = {
    "http": "socks5://localhost:9050",
    "https": "socks5://localhost:9050",
}

response = rq.get("http://ipinfo.io", proxies=proxies)
print(response.text)


# import socket
# import socks
#
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
# s = socks.socksocket()
# s.connect(('ipinfo.io', 80))
# s.sendall(b'GET / HTTP/1.1\r\nHost:ipinfo.io\r\n\r\n')
#
# data = ''
# buf = s.recv(1024)
# while len(buf):
#     data += buf.decode()
#     print(data)
#     buf = s.recv(1024)
# s.close()
