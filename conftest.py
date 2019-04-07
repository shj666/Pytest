import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commondata import commonData
http = HttpUtil()
@pytest.fixture(scope='session',autouse=True)
def session_fixture():
    path = "/sys/login"
    data = {"userName":"18210034706","password":"123456"}
    resp_login = http.post_login(path,data)
    commonData.token=resp_login['object']['token']
    print("登录成功")
