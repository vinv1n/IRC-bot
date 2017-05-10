import socket, re

global matrix

class bot:

    def __init__(self): #botin tiedot

        self.user = [':vinvin!vinvin@otitsun.oulu.fi']
        self.server = 'IRCnet'
        self.addr = "irc.oulu.fi"
        self.port = 6667
        self.nick = 'BotVinvin'
        self.realname = "BotVinvin"
        self.username = "BotVinvin"
        self.host = "IRC"

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #loppuja tietoja ei tarvitse määritellä
        #self.commands = botcommands.commands_dict

        self.channels = '#vinvin.testi'

    def message(self, msg):
        #lähettää viestin
        msg = msg + '\r\n'
        self.socket.send(msg.encode('utf-8'))

    def con(self):
        self.socket.connect((self.addr, self.port))
        self.socket.send('USER {} a a {}\r\n'.format(self.username,self.realname).encode('utf-8'))
        self.socket.send('NICK {}\n'.format(self.nick).encode('utf-8'))

        self.socket.send('JOIN {}\n'.format(self.channels).encode('utf-8')) #joining to channels
        print('Yhdistetty serverille {}'.format(self.addr))

    def ping(self, data):
        self.socket.send('PONG {}\r\n'.format(data[1]))

    def rec(self):
        data = self.socket.recv(4096)
        data = data.decode('utf-8')
        data.split('\r\n')
        return data

    def comm(self):
        data = self.rec()
        print(data)

    def input(self):
        while(True):
            data = self.rec()
            if (data.find('PING') != -1):
                self.ping(data)
            else:
                self.comm()


    def matrix1(self):
        matrix = [[0 for i in range(71)] for j in range(53)]
        for h in range(71):
            for k in range(53):
                matrix[k][h] = 'black'
        return matrix

class snake:

    def __init__(self):

        self.head = (0,4,'white')
        self.tail = (0,0, 'white')
        self.length = 5
        self.position = [(0 ,0, 'white'), (0, 1, 'white'), (0, 2, 'white') ,(0, 3, 'white') , (0 ,4, 'white')]
        self.buffer = []

    def move(self, msg, matrix):
        color = ['black', 'green', 'blue', 'white', 'yellow', 'red', 'cyan', 'magenta']
        msg = re.split('-|\s', msg)
        print(msg)
        if msg[2] in color and len(msg) == 3:
            try:
                matrix[int(msg[1])][int(msg[0])] = msg[2]
            except IndexError:
                print('paska!!')
            except ValueError:
                print('paska!?!')
            else:
                self.head = (int(msg[1]), int(msg[0]), msg[2])
                print(self.head)




if __name__ == "__main__":
    msg = '56-20 cyan'
    botti = bot()
    snake = snake()
    #botti.con()
    #botti.input()
    matrix = botti.matrix1()
    snake.move(msg, matrix)