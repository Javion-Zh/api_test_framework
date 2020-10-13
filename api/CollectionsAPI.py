"""
    被 case 调用
    实现收藏与取消收藏业务
"""
import app


class Collections:

    def __init__(self):
        self.collec_url = app.BASE_URL + "article/collections"

    def collec(self, session, id):
        # 设置提交 token 的信息头,使用参数 headers
        # {"Content-Type":"application/json","Authorization":"Bearer TOKEN的值"}
        my_headers = {"Content-Type": "application/json",
                      "Authorization": "Bearer " + app.TOKEN}
        return session.post(self.collec_url, json={"target": id}, headers=my_headers)
