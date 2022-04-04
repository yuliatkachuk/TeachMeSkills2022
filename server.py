import socket
import select

FOR_READ = list()
FOR_WRITE = list()

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 7899

srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv_socket.bind((SERVER_HOST, SERVER_PORT))
srv_socket.listen(3)


srv_socket.setblocking(False)
FOR_READ.append(srv_socket) # записываем сокеты на чтение


BUFFER_MSG = {}  #словарь для хранения сообщений от сокетов

while True:
    reads, writes, ERR = select.select(FOR_READ, FOR_WRITE, FOR_READ)
    for r in reads:
        if r is srv_socket:
            # серверный сокет и client хочет подключить кого-то нового
            # принимаем подключение
            client, address = r.accept()
            #устанавливаем неблокирующий сокет
            client.setblocking(False)
            # помещаем нового сlient в очередь на прослушивание
            if client not in FOR_READ:
                FOR_READ.append(client)
                print('Connection is successful: {}'.format(address))
        else:
            # иначе client хочет послать сообщение
            # читаем сообщение от client
            data = r.recv(2048)
            if data:
                # записываем в словарь сообщение data.decode("utf-8") с указанием сокета client
                BUFFER_MSG[r.fileno()] = data.decode('utf-8')  # ключ словаря - файловый дескриптор r.fileno()
                print(data.decode('utf-8'))
                if r not in FOR_WRITE:
                    FOR_WRITE.append(r)
            else:
                print('Клиент отключился...')
                if r in FOR_WRITE:
                    FOR_WRITE.remove(r)
                FOR_READ.remove(r)
                r.close()
                del BUFFER_MSG[r.fileno()]

    for w in writes:
        for key, value in BUFFER_MSG.items():
            data = value+' --- '
            #print(value)
           # if data:
            #отправляем сообщение
            w.send(data.encode('utf-8'))
            # удаляем из очереди на вывод\отправку сообщений
            # но оставляем в FOR_READ, вдруг захочет что-то написать
            #else:
        FOR_WRITE.remove(w)

    for e in ERR:
        print('клиент покинул чат'.format(e))
        #удаляем сокет с ошибкой из обеих очередей
        FOR_READ.remove(e)
        if e not in FOR_WRITE:
            FOR_WRITE.remove(e)
        # закрываем сокет, удаляем сообщения
        e.close()
        del BUFFER_MSG[e.fileno()]
