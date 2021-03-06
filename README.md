﻿===========
PyFalconUDP
===========

FalconUDP is an application level protocol for sending and receiving small messages (one to one thousand or more bytes) frequently (once a minute to hundreds of times a second) to and from one or many connected peers. It has been implemented on top of the Internet User Datagram protocol (UDP). 

PyFalconUDP is the official Python implementation. Throughout this module "FalconUDP" is used interchangeably to refer to the protocol or this Python implementation.

Project Status: Under Development, Pre-Alpha
============================================

Features
--------
* *Authentication and connection orientated.* FalconUDP only communicates with previously authenticated peers.
* *In-order and/or reliable messages.* Messages can be sent in-order, reliably, both in-order and reliable, or without any reliable and in-order checking and controls. Duplicates are always detected and dropped.
* *Minimal overhead.* FalconUDP adds minimal data to the user-application's data to be sent and received "on the wire" and includes support for "packing" additional user-application packets into existing outgoing messages.
* *Latency estimation*. FalconUDP measures round-trip-times from sending reliable messages till receiving the corresponding ACKnowlodgment, providing one way latency estimation to each connected peer.
* *Any Topology.* User-applications can use any logical network topology such as Server-Client or Peer-to-Peer.
* *Discovery.* FalconUDP peers can "discover" other FalconUDP peers on the same subnet (if a FalconUDP peer is set to accept discovery requests and optionally the request has a valid token).
* *NAT Traversal.* Two FalconUDP peers behind NAT(s) can establish a connection with each other after connecting to third publically accessible server to negotiate the connection.
* *Minimal garbage.* FalconUDP makes extensive use of memory management techniques to avoid creating garbage such as: pooling objects, segmenting buffers from large ones (to prevent heap memory fragmentation) and copying data directly into and out of buffers.
* *Statistics.* Total bytes per second sent and received to/from all remote peers.
Simulate latency, jitter and packet loss options.

Limitations
-----------
* Currently only IPv4 supported.\*
* No Congestion Control. FalconUDP provides no in-built congestion control.†
* No Encryption. FalconUDP has no in-built encryption.†

\*IPv6 planned 
†User-applications can use their own implementation before sending and after receiving data using the library's API.