import json
import unittest
#创建测试类
import requests
from parameterized import parameterized

import app
from api.loginAPI import Login
from app import PRO_PATH


#参数化数据解析
def read_json_file():
    data = []
    with open(PRO_PATH + "/data/login_data.json","r",encoding="utf-8") as f:
        for v in json.load(f).values():
            mobile = v.get("mobile")
            password = v.get("password")
            success = v.get("success")
            code = v.get("code")
            message = v.get("message")
            ele = (mobile,password,success,code,message)
            data.append(ele)
    return data

#创建登陆测试类
class TestLogin(unittest.TestCase):
    #
    def setUp(self):
        self.session = requests.Session()
        #创建登陆类对象
        self.login = Login()

    def tearDown(self):
        self.session.close()

    #参数化的调用
    @parameterized.expand(read_json_file())
    #登陆测试
    def test_login(self,mobile,password,success,code,message):
        # response1=request.Session.post(url)
        response1 = self.login.login_func(self.session,mobile,password)
        # print("响应体：",response1.json())
        #断言
        self.assertEqual(success,response1.json().get("success"))
        self.assertEqual(code, response1.json().get("code"))
        self.assertIn(message, response1.json().get("message"))
    #登陆成功测试
    def test_login_success(self):
        response2 = self.login.login_func(self.session,"13800000002","123456")
        self.assertIn("操作成功", response2.json().get("message"))
        self.assertEqual(True, response2.json().get("success"))
        self.assertEqual(10000, response2.json().get("code"))

        token = response2.json().get("data")
        app.TOKEN = token





if __name__ == '__main__':
    unittest.main()

