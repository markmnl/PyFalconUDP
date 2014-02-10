class LogLevel():
    """Severity of a log entry."""

    All         = 1
    Debug       = 2
    Info        = 3
    Warning     = 4
    Error       = 5
    Fatal       = 6
    NoLogging   = 7

class PacketType():
    """FalconUDP Packet Type"""

    ACK                 = 1
    ANTI_ACK            = 2
    JOIN_REQUEST        = 3
    ACCEPT_JOIN         = 4
    PING                = 5
    PONG                = 6
    APPLICATION         = 7
    DISCOVERY_REQUEST   = 8
    DISCOVERY_REPLY     = 9
    BYE                 = 10
    KEEP_ALIVE          = 11

class SendOptions():
    """Sequentiality and reliability control options for the delivery of a 
       packet."""

    RELIABLE            = 16
    IN_ORDER            = 32
    RELIABLE_IN_ORDER   = 48
    NONE                = 64





