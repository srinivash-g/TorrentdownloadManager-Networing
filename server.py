import socket
from qbittorrent import Client
qb = Client("http://127.0.0.1:1000/")
qb.login("admin", "adminadmin")
LocalHost="127.0.0.1"
port=8080
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((LocalHost,port))
server.listen(1)

print("Server is started")
print("Waiting for client request")
i=0
while i<2:
    clientConnection,clientAddress=server.accept()
    print("Connected client",clientAddress)
    tm=clientConnection.recv(1024)
    torm=tm.decode()
    tname=clientConnection.recv(1024)
    t1=tname.decode()
    print("Name:",t1)
    if torm=='Torrent File':        
       torrent_file = open(t1, "rb")
       #torrent_file = open("123.torrent", "rb")    
       qb.download_from_file(torrent_file)
    if torm=='Magnet Link':
        qb.download_from_link(t1)   
    qb.pause_all()
    qb.resume_all()
    print("The file has started downloading")
    def get_size_format(b, factor=1024, suffix="B"):
    
        for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
            if b < factor:
              return f"{b:.2f}{unit}{suffix}"
            b /= factor
        return f"{b:.2f}Y{suffix}"

        # return list of torrents
    torrents = qb.torrents()

    for torrent in torrents:
        print("Torrent name:", torrent["name"])
        print("hash:", torrent["hash"])
        print("Seeds:", torrent["num_seeds"])
        print("File size:", get_size_format(torrent["total_size"]))
        print("Download speed:", get_size_format(torrent["dlspeed"]) + "/s")
        clientConnection.send(str(torrent["name"]).encode('utf8'))
    i=i+1
server.close()

