"""
    封装请求业务，需要被 case 调用
"""
import app


class Articles:

    def __init__(self):
        self.get_articles_url = app.BASE_URL + "articles"


    def get_articles(self,session,id):
        my_id = {"channel_id":id}
        return session.get(self.get_articles_url,params=my_id)
