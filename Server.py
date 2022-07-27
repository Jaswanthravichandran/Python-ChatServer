import socket as soc
import select
#import banner
import sys

#banner()

#Setting up the host and port number
#Set host as empty it will work even machine ip is changed 

host = ''
port = 9999
socket_list = []
port_str = str(port)
receive_buffer = 4096

#Function for chat server
#..Here we create a socket object
#...Then we bind host and port 
#....Then we start to listing for incoming connection

def chat_server():
	server_socket = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
	server_socket.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
	server_socket.bind((host,port))
	server_socket.listen()
	socket_list.append(server_socket)
	print(f"Chat server started, listing on port {port_str}")

	while True:
		#It will check again and again
		#Blocking the flow for new imcoming connection...
		ready_read, ready_write, error = select.select(socket_list, [], [], 0)

		for sock in ready_read:

			if sock == server_socket:
				client_socket, addr = server_socket.accept()
				socket_list.append(client_socket)
				print(f"Client {addr} is connected !")
				broadcast(server_socket, client_socket, "{} Enetred our chatroom...\n".format(addr))
			else:
				try:
					data = sock.recv(receive_buffer)
					if data :
						broadcast(server_socket, sock, "[{}] {}".format(sock.getpeername(), data))
					else:
						#Socket maybe broken, so it remove the socket from the list.
						broadcast(server_socket, sock, "[{}] {}".format(sock.getpeername(), "Client is offline...\n"))
						if sock in socket_list:
							socket_list.remove(sock)
						
				except:
					broadcast(server_socket, sock, "[{}] {}".format(sock.getpeername(), "Client is offline...\n"))
					continue
		#TODO: Plan exit startegy
		server_socket.close()

def broadcast(server_socket,client_sock,message):
	for socket in socket_list:
		if socket != server_socket and socket != client_sock:
			try:
				socket.send(message)
			except:
				#socket might be broken so close the connection..
				socket.close()
				if socket in socket_list:
					socket_list.remove(socket)


if __name__ == "__main__":
	sys.exit(chat_server())
 