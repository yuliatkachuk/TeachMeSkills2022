import socket


SRV_HOST = '127.0.0.1' #socket.gethostname()
SRV_PORT =  7899

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SRV_HOST, SRV_PORT))
    name = input('Enter your name: ')
    client.send((name + ' connected to chat').encode('utf-8'))  # Уведомляем сервер о подключении
    name1 = name + '>>> '

    while True:
        message = input(name1)
        if message=='QUIT':
            message = name1.encode('utf-8') + message.encode('utf-8')
            client.send(message)
            break
        elif message in ['r', 'refresh']:
            print(client.recv(2048).decode('utf-8'))
        else:
            message = name1.encode('utf-8') + message.encode('utf-8')+ '    '.encode('utf-8')
            client.send(message)
            #client.recv(2048).decode('utf-8')

    print(client.recv(2048).decode('utf-8'))
    print('server>>> ', name + ',', 'bye-bye!')
except BaseException as err:
    print('Ничего не вышло', err)