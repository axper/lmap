import psutil


def connection_status_is_listen_and_ip_is_not_localhost(connection):
    return connection.status == 'LISTEN' #and connection.laddr[0] != '::' and connection.laddr[0] != '127.0.0.1'


def main():
    for connection in psutil.net_connections(kind='inet'):
        if connection_status_is_listen_and_ip_is_not_localhost(connection):
            print(connection.family, connection.laddr, connection.pid)
            process = psutil.Process(connection.pid)
            print(process, '\n',
                  'parent: ', process.ppid(), '\n',
                  'name: ', process.name(), '\n',
                  'exe: ', process.exe(), '\n',
                  'cmdline: ', process.cmdline(), '\n',
                  'create_time: ', process.create_time(), '\n',
                  'parent: ', process.parent(), '\n',
                  'cwd: ', process.cwd(), '\n',
                  'username: ', process.username(), '\n',
                  'terminal: ', process.terminal(), '\n',
                  'nice: ', process.nice(), '\n',
                  'num_threads: ', process.num_threads(), '\n',
                  'memory_info: ', process.memory_info(), '\n',
                  'children: ', process.children(), '\n',
                  )


if __name__ == "__main__":
    main()
