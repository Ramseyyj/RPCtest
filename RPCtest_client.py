import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://192.168.159.129:8000')
print(s.pow(2,3))  # Returns 2**3 = 8
print(s.add(2,3))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10
print(s.getTime())

# Print list of available methods
print(s.system.listMethods())