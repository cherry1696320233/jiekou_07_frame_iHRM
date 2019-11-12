from app import BASE_URL


class Login:

    def __init__(self):
        self.login_url = BASE_URL + "/api/sys/login"
    #登陆请求封装方法
    def login_func(self,session,mobile,password):
        my_login_data = {"mobile":mobile, "password":password}
        return session.post(self.login_url,json=my_login_data)