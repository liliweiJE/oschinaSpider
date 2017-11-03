import multiprocessing
import socket
import time
import re
import requests
from bs4 import BeautifulSoup


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname("openbarrage.douyutv.com")
port = 8601
client.connect((host, port))

danmu_path = re.compile(b'txt@=(.+?)/cid@')
uid_path = re.compile(b'uid@=(.+?)/nn@')
nickname_path = re.compile(b'nn@=(.+?)/txt@')
level_path = re.compile(b'level@=([1-9][0-9]?)/sahf')

def sendmsg(msgstr):
    msg = msgstr.encode('utf-8')
    data_length = len(msg) + 8
    code = 689
    msgHead = int.to_bytes(data_length, 4, 'little') \
              + int.to_bytes(data_length, 4, 'little') + int.to_bytes(code, 4, 'little')
    client.send(msgHead)
    sent = 0
    while sent < len(msg):
        tn = client.send(msg[sent:])
        sent = sent + tn


def start(roomid):
    msg = 'type@=loginreq/username@=rieuse/password@=douyu/roomid@={}/\0'.format(roomid)
    sendmsg(msg)
    msg_more = 'type@=joingroup/rid@={}/gid@=-9999/\0'.format(roomid)
    sendmsg(msg_more)

    print('---------------欢迎连接到{}的直播间---------------'.format(get_name(roomid)))
    while True:
        data = client.recv(1024)
        uid_more = uid_path.findall(data)
        nickname_more = nickname_path.findall(data)
        level_more = level_path.findall(data)
        danmu_more = danmu_path.findall(data)
        if not level_more:
            level_more = b'0'
        if not data:
            break
        else:
            for i in range(0, len(danmu_more)):
                try:
                    product = {
                        'uid': uid_more[i].decode(encoding='utf-8'),
                        'nickname': nickname_more[i].decode(encoding='utf-8'),
                        'level': level_more[i].decode(encoding='utf-8'),
                        'danmu': danmu_more[i].decode(encoding='utf-8')
                    }
                    print(product)
                    #print('成功导入mongodb')
                except Exception as e:
                    print(e)


def keeplive():
    while True:
        msg = 'type@=keeplive/tick@=' + str(int(time.time())) + '/\0'
        sendmsg(msg)
        time.sleep(15)


def get_name(roomid):
    r = requests.get("http://www.douyu.com/" + roomid)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find('a', {'class', 'zb-name'}).string


if __name__ == '__main__':
    room_id = input('请出入房间ID： ')
    p1 = multiprocessing.Process(target=start, args=(room_id,))
    p2 = multiprocessing.Process(target=keeplive)
    p1.start()
    p2.start()