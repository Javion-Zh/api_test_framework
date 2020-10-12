"""
    封装登录相关业务实现:
        1.短信验证码请求
        2.登录请求
"""
#创建类
    #__init__函数，封装 URL
    #请求业务函数1:获取验证码
    #请求业务函数2:登录
import app


class Login:

    def __init__(self):
        self.get_code_url = app.BASE_URL + "sms/codes/"
        self.login_url = app.BASE_URL + "authorizations"

    # 验证码获取
    def get_code(self,session,mobile):
        return session.get(self.get_code_url + mobile)


    #登录函数
    def login(self,session,mobile,code):
        # my_login = {"mobile":mobile,
        #             "code":code}
        my_login = {}
        if mobile:
            my_login["mobile"] = mobile
        if code:
            my_login["code"] = code
        return session.post(self.login_url,json=my_login)

