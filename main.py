import psutil
from socket import SOCK_STREAM
from socket import SOCK_DGRAM


def port_is_open_and_externally_accessible(connection):
    # If TCP
    if connection.type == SOCK_STREAM:
        return connection.status == 'LISTEN'
    # If UDP
    if connection.type == SOCK_DGRAM:
        return True


def main():
    for connection in psutil.net_connections(kind='inet'):
        if port_is_open_and_externally_accessible(connection):
            print('family=', connection.family, 'type=', connection.type, 'laddr=', connection.laddr, 'pid=',
                  connection.pid)
            # print(connection)
            if connection.pid is not None:
                process = psutil.Process(connection.pid)
                print(process, '\n',
                      # 'parent: ', process.ppid(), '\n',
                      # 'name: ', process.name(), '\n',
                      # 'exe: ', process.exe(), '\n',
                      'cmdline: ', process.cmdline(), '\n',
                      # 'create_time: ', process.create_time(), '\n',
                      # 'parent: ', process.parent(), '\n',
                      # 'cwd: ', process.cwd(), '\n',
                      'username: ', process.username(), '\n',
                      # 'terminal: ', process.terminal(), '\n',
                      # 'nice: ', process.nice(), '\n',
                      'num_threads: ', process.num_threads(), '\n',
                      # 'memory_info: ', process.memory_info(), '\n',
                      # 'children: ', process.children(), '\n',
                      )
            else:
                print('Unknown PID', '\n')


if __name__ == "__main__":
    main()
