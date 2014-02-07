import socket
import datetime
from falconudp.enums import LogLevel

class FalconPeer():
    """Represents a FalconUDP peer which can discover, join and communicate 
       with other compatible FalconUDP peers reachable on the same network. """

    def __init__(self, port=37896, log_level=LogLevel.Info):
        self._port = port
        self._log_level = log_level

    def _log(self, log_level, msg):
        if(log_level >= self._log_level):
            line = '{0:%Y-%m-%d %H:%M:%S}\t{1}\t{2}\t{3}'.format(datetime.datetime.now(), 
                                                        self._port,
                                                        log_level, 
                                                        msg)
            print(line) # TODO log instead


    def _check_started(self):
        if not hasattr(self, '_started') or not self._started:
            raise Exception('not started')

    def _process_data(self, data):
        pass
    
    def _recv(self):
        self.check_started()
        (data, addr) = self._socket.recvfrom(1024)
        process_data(data)

    def start(self):
        """TODO"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', self._port))
        sock.listen(0) # presumably this is irrelevant for dgram sockets?
        self._socket = sock
        self._started = True
        _log(LogLevel.Info, 'Started, listening on port: {0}.'.format(_port))

    def stop(self):
        """TODO"""
        _check_started()
        # TODO
        self._started = False
        _log(LogLevel.Info, 'Stopped.')




