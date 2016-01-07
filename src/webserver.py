import socket,re

HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	pt = re.compile(r'GET /(.*?) HTTP',re.S)
	match = pt.findall(request)
	
	http_response = """{
	"code":"-1", 
	"msg":"Access Denied", 
	"data":""
}
"""
	if len(match) != 0 and match[0] == 'get':
		http_response = """{
	"code":"0", 
	"msg":"success", 
	"data":""
}
"""
	
	client_connection.sendall(http_response)
	client_connection.close()

