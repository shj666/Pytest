# from common.commondata import commonData
# from conftest import http
# import allure
# @allure.feature('修改密码模块')
# class Test_login():
#     def setUp(this):
#         pass
#     def test_login_success(this):
#        data={"userName":commonData.username,"password":commonData.passWord}
#        resp = http.post_login("/sys/login",data)
#        assert resp['code']==200
#        assert resp['msg']=='操作成功'
#        assert resp['object']['userId']== 201
#        print(resp)
#     @allure.story('修改密码成功')
#     def test_changepwd_success(this):
#         data={"userId":'201',"userName":commonData.username,"oldPwd":commonData.passWord,"password":commonData.passWord1}
#         resp = http.post_login("/sys/changePwd", data)
#         # resp = ("http://192.168.1.203:8083/sys/changePwd",data)
#         assert resp['code'] == 200
#         assert resp['msg'] == '操作成功'
#         print(resp)
#     def tearDown(this):
#         pass
#     # def test_changepwd_success_back(this):
#     #     data={"userId":'201',"userName":commonData.username,"oldPwd":commonData.passWord1,"password":commonData.passWord}
#     #     resp = http.post_login("/sys/changePwd", data)
#     #     # resp = ("http://192.168.1.203:8083/sys/changePwd",data)
#     #     assert resp['code'] == 200
#     #     assert resp['msg'] == '操作成功'
#     #     print(resp)
#     # def test_changepwd_fail(this):
#     #     data={"userId":'201',"userName":commonData.username,"oldPwd":commonData.passWord,"password":''}
#     #     resp = http.post_login("/sys/changePwd", data)
#     #     # resp = ("http://192.168.1.203:8083/sys/changePwd",data)
#     #     assert resp['code'] == 200
#     #     assert resp['msg'] == '操作成功'
#     #     print(resp)
#     # def test_changepwd_fail2(this):
#     #     data={"userId":'201',"userName":commonData.username,"oldPwd":commonData.passWord1,"password":commonData.passWord1}
#     #     resp = http.post_login("/sys/changePwd", data)
#     #     # resp = ("http://192.168.1.203:8083/sys/changePwd",data)
#     #     assert resp['code'] == 411
#     #     assert resp['msg'] == '旧密码错误'
#     #     print(resp)