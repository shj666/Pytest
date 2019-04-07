import requests
import json
from common.commondata import commonData
class HttpUtil:
    def __init__(self):
        self.http = requests.session()
        self.headers={'Content-Type':'application/json;charset=UTF-8'}
    def post_login(self,path,data):
        proxies = commonData.proxies
        host = commonData.host
        data_json = json.dumps(data)
        if commonData.token is not None:
            self.headers['token']=commonData.token
        resp_login = self.http.post(url=host+path, proxies=proxies,
                               data=data_json, headers=self.headers)
        assert resp_login.status_code ==200
        resp_json = resp_login.text
        resp_dict = json.loads(resp_json)
        return resp_dict
    # def post_loginout(self):
    #     proxies = {'http': 'http://localhost:8888'}
    #     headers = {}
    #     headers['Content-Type'] = 'application/json;charset=UTF-8'
    #     headers['token'] = self.token
    #     self.data = {'token': self.token}
    #     resp_loginout = self.http.post(url="http://192.168.1.203:8083/sys/logout", proxies=proxies, data="", headers=headers)
    #     return resp_loginout
# resp=requests.get("http://www.baidu.com")
# print(resp.text)
# resp1=requests.get("http://192.168.1.112/dvwa")
# print(resp1.text)
# print(resp1.headers)
# print(resp1.cookies)
# print(resp1.url)
# print(resp1.status_code)
# proxies = {'http':'http://localhost:8888'}
# headers={}
# headers['Content-Type']='application/json;charset=UTF-8'
# http=requests.session()
# resp = http.post(url="http://192.168.1.203:8083/sys/login",proxies=proxies,data='{"userName":"18210034706","password":"123456"}',headers=headers)
# resp_dict = json.loads(resp.text)  #json转python_dict
# token = resp_dict['object']['token'] #获取token
# headers['token']=token   #将token加到headers_dict里
# data= {'token':token}  #创建一个datadict的，添加了token的数据
# data_json = json.dumps(data)  #将python对象转成json
# resp = http.post(url="http://192.168.1.203:8083/sys/getUserInfo",proxies=proxies,data=data_json,headers=headers)
# print(resp.text)
#print(resp.text)
# print(resp.headers)
# print(resp.cookies)
# print(resp.url)
# print('http code',resp.status_code)
