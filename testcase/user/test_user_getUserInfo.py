from common.commondata import commonData
from conftest import http
import allure
@allure.feature('获取用户信息模块')
class Test_login():
    # def test_loaduserinfo_success(self):
    #     path = '/userveOrUpdateUser'
    #     data = {'nickName': '1996',
    #             'userName': '15011111111',
    #             'telNo': '', 'email': '', 'address': '', 'roleIds': '', 'regionId': 1, 'regionLevel': 1}
    #     resp = http.post(path, data)
    #     assert resp['code'] == 401
    #     assert resp['msg'] == '无权限访问'
    #     print(resp)

    def test_login_success(this):
       data={"userName":commonData.userName,"password":commonData.password}
       resp = http.post_login("/sys/login",data)
       assert resp['code']==200
       assert resp['msg']=='操作成功'
       assert resp['object']['userId']== 2
       print(resp)
    def test_region(this):
        data={"pageCurrent":'1',"pageSize":'10',"nickName":"","userName":"","regionId":'1'}
        resp = http.post_login("/user/loadUserList",data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print(resp)
    def test_login(this):
       data={"userName":'15011111111',"password":'123456'}
       resp = http.post_login("/sys/login",data)
       assert resp['code']==200
       assert resp['msg']=='操作成功'
       print(resp)
       resp_id = resp['object']['userId']
       print(resp_id)
    def test_user_getUserInfo(this):
        data = {"pageCurrent": '1', "pageSize": '1', "nickName": "", "userName": "", "regionId": '1'}
        resp = http.post_login("/user/loadUserList", data)
        resp_id = resp['object']['list'][0]['id']
        return resp_id
        resp_nickname = resp['object']['list'][0]['nickName']
        print(resp_id)
        print(resp_nickname)
        if resp_id == Test_login.test_login(resp_id):
            print("成功")
        else:
            print("失败")

    @allure.story('修改密码成功')
    def test_loadUserInfo(this):
        data={"id":this.test_user_getUserInfo()}
        resp = http.post_login("/user/loadUserInfo", data)
        assert resp['code'] == 200
        assert resp['msg'] == '操作成功'
        print(resp)
