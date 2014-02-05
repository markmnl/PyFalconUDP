import socket

class FalconPeer(object):

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', self._port))
        sock.listen(0) # presumably this is irrelevant for dgram sockets?
        self._socket = sock
        self._started = True

    def check_started(self):
        if not hasattr(self, '_started') or not self._started:
            raise Exception('not started')

    def process_data(self, data):
        pass

    def recv(self):
        self.check_started()
        (data, addr) = self._socket.recvfrom(1024)
        process_data(data)

    def __init__(self, port=37896):
        self._port = port



