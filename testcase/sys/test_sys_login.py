# from common.commondata import commonData
# from conftest import http
# class Test_login():
#     def test_login_success(this):
#        data={"userName":commonData.userName,"password":commonData.password}
#        resp = http.post_login("/sys/login",data)
#        assert resp['code']==200
#        assert resp['msg']=='操作成功'
#        assert resp['object']['userId']== 2
#        print(resp)
#     def test_login_fail1(this):#密码错误
#         data = {"userName": commonData.userName, "password":'111111'}
#         resp = http.post_login("/sys/login", data)
#         assert resp['code'] == 410
#         assert resp['msg'] == '用户名或密码错误'
#         print(resp)
#     def test_login_fail2(this):#用户名不存在    用户名15位
#         data = {"userName": '44444444444', "password": commonData.password}
#         resp = http.post_login("/sys/login", data)
#         assert resp['code'] == 301
#         assert resp['msg'] == '用户不存在'
#         print(resp)
#     def test_login_fail5(this):#用户名不存在    用户名15位
#         data = {"userName": '182100347061234', "password": commonData.password}
#         resp = http.post_login("/sys/login", data)
#         assert resp['code'] == 301
#         assert resp['msg'] == '用户不存在'
#         print(resp)
#     def test_login_fail3(this): #用户名为空
#         data = {"userName":commonData.userName1, "password": commonData.password}
#         resp = http.post_login("/sys/login", data)
#         assert resp['code'] == 200
#         assert resp['msg'] == '操作成功'
#         assert resp['object']['userId'] == 79
#         print(resp)
#     def test_login_fail4(this): #参数不存在
#         data = {"password": commonData.password}
#         resp = http.post_login("/sys/login", data)
#         assert resp['code'] == 301
#         assert resp['msg'] == '用户不存在'
#         assert resp['object'] == 'null'
#         print(resp)
#     def test_loginout(this):
#         path='/sys/logout'
#         data = {'token': commonData.token}
#         resp = http.post_login(path, data)
#         print(resp)