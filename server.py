 #!/usr/bin/env python

import sys

from datetime import datetime

from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory

from twisted.internet import reactor
from twisted.python import log

from twisted.internet.task import LoopingCall

class MyServer(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")
        lc = LoopingCall(self.sendTime)
    	lc.start(5)

    def onMessage(self, payload, isBinary):
    	#You can treat text and binary messages here
    	if (isBinary):
    		print "Binary message received!"
    	else:
        	print "Message received: %s" % payload

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

    def sendTime(self):
    	self.sendMessage(str(datetime.now()), isBinary=False)

if __name__ == '__main__':

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory("ws://0.0.0.0:9000", debug=False)
    factory.protocol = MyServer
    # factory.setProtocolOptions(maxConnections=2)

    reactor.listenTCP(9000, factory)
    reactor.run() 