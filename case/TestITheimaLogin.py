"""
    测试登录实现:
        1.获取短信验证码接口
        2.登录接口

    知识点:
        1.实现请求业务的封装 === case 调用 api
        2.实现参数化 === case 解析 data
"""
# 导包
import json
import unittest
import requests
from parameterized import parameterized
# 创建测试类
    #初始化函数
    #卸载函数
    #测试函数1:短信验证码获取
    #测试函数2:登录
import app
from api.LoginAPI import Login

def read_from_json():
    # 创建空列表
    data = []
    # 读文件，将读取的数据追加进列表
    with open(app.BASE_PATH + "/data/login_data.json","r",encoding="utf-8") as f:
        for value in json.load(f).values():
            # 分别获取手机号、验证码、状态码、提示信息
            mobile = value.get("mobile")
            code = value.get("code")
            status_code = value.get("status_code")
            message = value.get("message")
            # 添加至元组
            ele = (mobile,code,status_code,message)
            # 追加进列表
            data.append(ele)
    # 返回列表
    return data
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.login_obj = Login()
    def tearDown(self):
        self.session.close()

    #测试函数1:获取验证码
    def test_get_code(self):
        # 1.调用 api 的请求业务
        response = self.login_obj.get_code(self.session,"13012345679")
        # 2.断言
        print(response.json())
        self.assertIn("OK",response.json().get("message"))

    #测试函数2:登录
    def test_login(self):
        # 1.调用 api 的请求业务
        response = self.login_obj.login(self.session,"13911111111","246810")
        # 2.断言
        self.assertEqual(201,response.status_code)
        self.assertIn("OK",response.json().get("message"))
        print(response.status_code)
        print(response.json())
        # 获取响应的身份标记: token
        app.TOKEN = response.json().get("data").get("token")
        print("获取到的 token:",app.TOKEN)

    #测试函数3: 参数化导入数据
    @parameterized.expand(read_from_json())
    def test_login_params(self,mobile,code,status_code,message):
        print("-"*100)
        print(mobile,code,status_code,message)
        # 1.登录业务
        response = self.login_obj.login(self.session,mobile,code)
        # 2.断言业务
        self.assertEqual(status_code,response.status_code)
        self.assertIn(message,response.text)
