import hashlib
import sys

#server_list = ['server001', 'server002', 'server003', 'server004', 'server005', 'server006', 'server007', 'server008', 'server009', 'server010', 'server011', 'server012']

server_list = []
for i in range (1,100):
    server_name = 'server'+str(i)
    server_list.append(server_name)


print(server_list)

NUM_OF_BUCKS = 2
SUM = 0
for server in server_list:
    #print(server)
    md5hash = hash(server)
    if md5hash < 0:
        md5hash +=  sys.maxsize
    #print(md5hash)
    bucket_value = md5hash % NUM_OF_BUCKS
    SUM = SUM + bucket_value
    print(bucket_value)

print(SUM)
