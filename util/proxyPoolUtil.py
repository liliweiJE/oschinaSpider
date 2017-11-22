import requests

class ProxyPoolUtil(object):
    @staticmethod
    def get_proxy():
        return requests.get("http://127.0.0.1:5010/get/").content

    @staticmethod
    def delete_proxy(proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))