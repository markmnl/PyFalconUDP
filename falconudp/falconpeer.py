import socket
import datetime
from falconudp.enums import LogLevel

FALCON_VERSION                  = 1
MAX_DATAGRAM_SIZE               = 1024 - 33
FALCON_PACKET_HEADER_SIZE       = 5
ADDITIONAL_PACKET_HEADER_SIZE   = 3
PACKET_TYPE_MASK                = 15
SEND_OPTS_MASK                  = 112


class FalconPeer():
    """Represents a FalconUDP peer which can discover, join and communicate 
       with other compatible FalconUDP peers reachable on the same network. """

    def __init__(self, port=37896, log_level=LogLevel.Info):
        self._port = port
        self._log_level = log_level
        self._recv_buffer = bytearray(MAX_DATAGRAM_SIZE)
        self._recv_memview = memoryview(self._recv_buffer)

    def _log(self, log_level, msg):
        if(log_level >= self._log_level):
            line = '{0:%Y-%m-%d %H:%M:%S}\t{1}\t{2}\t{3}'.format(datetime.datetime.now(), 
                                                        self._port,
                                                        log_level, 
                                                        msg)
            print(line) # TODO log instead

    def _check_started(self):
        if not hasattr(self, '_started') or not self._started:
            raise Exception('not started!')

    def _drop_peer(self, addr, say_bye, reason):
        if addr in self._peers:
            if say_bye:
                pass #TODO 
            del self._peers[addr]
            _log(LogLevel.Info, 'dropped {0}, {1}'.format(addr, reason))

    def _recv(self):
        self.check_started()
        (size, addr) = self._socket.recvfrom_into(self._recv_memview, MAX_DATAGRAM_SIZE)
        if size == 0:
            self._drop_peer(addr, False, 'peer disconnected')
            return;
        elif size < FALCON_PACKET_HEADER_SIZE or size > MAX_DATAGRAM_SIZE:
            self._drop_peer(addr, False, 'bad size datagram')
            return;
        else:
            while True:
                byte = self._recv_buffer[0]
                type = byte & PACKET_TYPE_MASK
                opts = byte & SEND_OPTS_MASK
                seq = int.from_bytes(self._recv_buffer[1:3], 'little')
                payload_size = int.from_bytes(self._recv_buffer[3:5], 'little')
                if (FALCON_PACKET_HEADER_SIZE + payload_size) > size:
                    self._log(LogLevel.Warning, 'Dropped datagram from {0}, size {1} less than min purported {2}'.format(addr, size, FALCON_PACKET_HEADER_SIZE + payload_size))
                    return
                if addr in self._peers:
                    pass #TODO
                else:
                    pass #TODO
                size -= (FALCON_PACKET_HEADER_SIZE + payload_size)
                if size < ADDITIONAL_PACKET_HEADER_SIZE:
                    break


    def start(self):
        """TODO"""
        if hasattr(self, '_started') and self._started:
            raise Exception('already started!')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.bind((socket.INADDR_ANY, self._port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # allow broadcast TODO set later only if needed?
        self._socket = sock
        self._started = True
        self._peers = {}
        self._log(LogLevel.Info, 'Started, listening on port: {0}.'.format(self._port))

    def stop(self):
        """TODO"""
        self._check_started()
        # TODO say bye to all peers
        self._socket.close()
        self._started = False
        self._log(LogLevel.Info, 'Stopped.')




