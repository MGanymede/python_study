import os
from abc import ABC


import tornado.ioloop
import tornado.web
# from Tornado_study.fetcher.Rent import Rent
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from fetcher.Rent import Rent

rent = Rent()



class MainHandler(tornado.web.RequestHandler, ABC):
    @gen.coroutine
    def get(self):
        client = AsyncHTTPClient()
        response = yield client.fetch("http://www.baidu.com")
        print(dir(response))
        print(response.body)
        self.render("index.html", title="瑞祥爬虫系统")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ], static_path=os.path.join(os.path.dirname(__file__), "static"))


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
