import requests
import json
import inspect
from datetime import datetime
from json import JSONEncoder, JSONDecoder

class Web():
    #url = "http://www.raspberrypi.com.tw/pycon_tw/2015/code/handon-test.php"
    #url = "http://www.raspberrypi.com.tw/pycon_tw/2015/code/handon.php"
    url = "http://www.raspberrypi.com.tw/pycon_tw/2015/code/server.php"
    headers = {'content-type': 'application/json'}
    payload = None

    def __init__(self):
        self.encoder = JSONEncoder()
        self.decoder = JSONDecoder()

    class err():
        status_code = 999
        text = "exception"

    # payload : {"json":"http://playground.imagga.com/static/img/example_photo.jpg"}
    def get(self, payload):
        try:
            return requests.request("GET", self.url, headers=self.headers, params=payload)
        except requests.exceptions.RequestException as e:
            print e
            return self.err()

    def post(self, payload):
        try:
            #payload = json.dumps(payload)
            return requests.post(self.url, data=payload)
            #response = requests.post(url,params=data,headers=headers)
        except requests.exceptions.RequestException as e:
            print e
            return self.err()

    def registerUpdate(self, reg_no, uid):
        # reg_no = reg_no
        # uid = uid
        # regist_wtime = regist_wtime
        # return: True/False

        # test data
        # reg_no:
        # uid:
        # regist_wtime:
        try:
            #payload = json.dumps(payload)
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            payload = {'action':'regist-update', 'reg_no':reg_no, 'uid':uid, 'regist_wtime':now}
            result = requests.post(self.url, data=payload)

            return json.loads(result.text)
        except requests.exceptions.RequestException as e:
            print e
            return self.err()

    def tshirtQuery(self, uid):
        print type(self).__name__ + "/" + inspect.stack()[0][3]
        # uid = uid
        # return: (reg_no, nickname, tshirt, tshirt_wtime)

        # test data
        # uid: 09  4d  06  02
        payload = {"action": "tshirt-query", "uid": uid}

        try:
            req = requests.post(self.url, data=payload)

            if req.status_code != 200:
                print req.status_code
                return None

            print req.text
            return json.loads(req.text)
        except requests.exceptions.RequestException as e:
            print e
            return self.err()

    def tshirtUpdate(self, uid):
        # data = (uid, tshirt_wtime)
        # return: True/False

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        payload = {"action": "tshirt-update", "uid": uid, "tshirt_wtime": now}

        try:
            req = requests.post(self.url, data=payload)

            if req.status_code != 200:
                return None

            print req.text
            return json.loads(req.text)
        except requests.exceptions.RequestException as e:
            print e
            return self.err()


    def infoQuery(self, uid):
        # uid = uid
        # return: reg_no, uid, nickname, regist_wtime, tshirt_wtime
        payload = {"action": "query", "uid": uid}

        try:
            req = requests.post(self.url, data=payload)

            if req.status_code != 200:
                print req.status_code
                return None

            print req.text
            return json.loads(req.text)
        except requests.exceptions.RequestException as e:
            print e
            return self.err()

