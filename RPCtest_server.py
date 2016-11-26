import datetime
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("192.168.159.129", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()


# Register a function under a different name
def get_server_time():
    return datetime.datetime.now()
server.register_function(get_server_time, 'getServerTime')

print('server is ready for request!')

# Run the server's main loop
server.serve_forever()
