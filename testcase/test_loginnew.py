# import pytest
# import requests
# from common.commondata import commonData
# from conftest import http
# def test_loginnew():
#     path = '/sys/getUserInfo'
#     data = {'token':commonData.token}
#     resp = http.post_login(path,data)
#     print(resp)
# def test_loginout():
#     path='/sys/logout'
#     data = {'token': commonData.token}
#     resp = http.post_login(path, data)
#     print(resp)