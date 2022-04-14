import sys
import socket
import time

if len(sys.argv) < 3:
    print('usage : %s ip port' % (sys.argv[0]))
    exit()

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((sys.argv[1], int(sys.argv[2])))


def read_line(socket):
    content,c = '',' '
    while c and c!='\n':
        c = socket.recv(1)
        if c :
            c = c.decode('ascii', 'ignore')
            content += c
    return content

def send_instruction(socket, instruction):
    instruction += '\n'
    socket.send(instruction.encode('utf-8'))


# on parse le labyrinthe
def parse_labyrinthe(socket_client):
    labyrinthe = []
    line = read_line(socket_client)
    while len(line) > 10 :
        if line[0] == '$':
            line = line[2:]
        print(line, end='')
        labyrinthe.append(line[:-1][::2])
        line = read_line(socket_client)
    return labyrinthe

# on affiche la bianière
for i in range(20):
    line = read_line(socket_client)
    print(line, end='')

# on peut écrire l'algorithme ici (à modifier)
labyrinthe = parse_labyrinthe(socket_client)
send_instruction(socket_client, 'up')
labyrinthe = parse_labyrinthe(socket_client)
send_instruction(socket_client, 'up')
labyrinthe = parse_labyrinthe(socket_client)


# si on a réussi à atteindre la fin, on peut afficher le flag
for i in range(6):
    line = read_line(socket_client)
    print(line, end='')

socket_client.close()
