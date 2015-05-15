 #!/usr/bin/env python

from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

class MyServer(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
    	"""You can treat text and binary messages here"""
        pass

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


if __name__ == '__main__':

    import sys

    # This example uses Twisted for real-time web sockets.
    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory("ws://.0.0.0.0:9000", debug=False)
    factory.protocol = MyServer
    # factory.setProtocolOptions(maxConnections=2)

    reactor.listenTCP(9000, factory)
    reactor.run() 